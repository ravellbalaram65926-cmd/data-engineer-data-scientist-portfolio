import sqlite3
import tempfile
import unittest
from pathlib import Path

from src.main import DATA, build_warehouse


class WarehousePipelineTests(unittest.TestCase):
    def test_elt_is_repeatable_and_aggregates_in_sql(self):
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "warehouse.sqlite"
            self.assertEqual(build_warehouse(database, DATA), 3)
            self.assertEqual(build_warehouse(database, DATA), 3)
            connection = sqlite3.connect(database)
            try:
                row = connection.execute(
                    "SELECT order_count, lifetime_value FROM mart_customer_sales "
                    "WHERE customer_id = 'C001'"
                ).fetchone()
            finally:
                connection.close()
            self.assertEqual(row, (2, 77.5))


if __name__ == "__main__":
    unittest.main()
