"""ELT demo: load raw CSVs into SQLite, then model the warehouse with SQL."""

import argparse
import csv
import sqlite3
from contextlib import closing
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw"
DEFAULT_DB = ROOT / "data" / "warehouse.sqlite"


def load_csv(connection: sqlite3.Connection, table: str, path: Path, columns: tuple[str, ...]) -> None:
    with path.open(newline="", encoding="utf-8") as source:
        rows = csv.DictReader(source)
        placeholders = ",".join("?" for _ in columns)
        names = ",".join(columns)
        connection.executemany(
            f"INSERT OR REPLACE INTO {table} ({names}) VALUES ({placeholders})",
            (tuple(row[column] for column in columns) for row in rows),
        )


def build_warehouse(database: Path, data_dir: Path = DATA) -> int:
    database.parent.mkdir(parents=True, exist_ok=True)
    with closing(sqlite3.connect(database)) as connection, connection:
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS raw_customers (
                customer_id TEXT PRIMARY KEY, city TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS raw_orders (
                order_id TEXT PRIMARY KEY, customer_id TEXT NOT NULL,
                order_date TEXT NOT NULL, amount REAL NOT NULL
            );
            """
        )
        load_csv(connection, "raw_customers", data_dir / "customers.csv", ("customer_id", "city"))
        load_csv(
            connection,
            "raw_orders",
            data_dir / "orders.csv",
            ("order_id", "customer_id", "order_date", "amount"),
        )
        connection.executescript(
            """
            CREATE VIEW IF NOT EXISTS stg_orders AS
            SELECT order_id, customer_id, date(order_date) AS order_date,
                   CAST(amount AS REAL) AS amount
            FROM raw_orders
            WHERE amount >= 0;
            CREATE TABLE IF NOT EXISTS mart_customer_sales (
                customer_id TEXT PRIMARY KEY, city TEXT NOT NULL,
                order_count INTEGER NOT NULL, lifetime_value REAL NOT NULL,
                latest_order_date TEXT
            );
            DELETE FROM mart_customer_sales;
            INSERT INTO mart_customer_sales
            SELECT c.customer_id, c.city, COUNT(o.order_id),
                   ROUND(COALESCE(SUM(o.amount), 0), 2), MAX(o.order_date)
            FROM raw_customers AS c
            LEFT JOIN stg_orders AS o ON o.customer_id = c.customer_id
            GROUP BY c.customer_id, c.city;
            """
        )
        return connection.execute("SELECT COUNT(*) FROM mart_customer_sales").fetchone()[0]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=DEFAULT_DB)
    parser.add_argument("--data-dir", type=Path, default=DATA)
    args = parser.parse_args()
    count = build_warehouse(args.database, args.data_dir)
    print(f"Built {count} customer mart rows in {args.database}")


if __name__ == "__main__":
    main()
