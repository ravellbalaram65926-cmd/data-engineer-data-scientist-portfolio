"""ETL demo: validate daily sales and build lag/rolling forecast features."""

import argparse
import csv
from collections import deque
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "raw" / "sample_sales.csv"
DEFAULT_OUTPUT = ROOT / "data" / "gold" / "forecast_features.csv"


def build_features(input_path: Path) -> list[dict[str, str]]:
    with input_path.open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))
    rows.sort(key=lambda row: (row["store_id"], row["item_id"], row["date"]))
    histories: dict[tuple[str, str], deque[int]] = {}
    seen: set[tuple[str, str, str]] = set()
    result = []
    for row in rows:
        key = (row["store_id"], row["item_id"], row["date"])
        if key in seen:
            continue
        seen.add(key)
        date.fromisoformat(row["date"])
        units = int(row["units"])
        price = float(row["unit_price"])
        if units < 0 or price < 0:
            raise ValueError(f"Negative units or price in row {key}")
        history = histories.setdefault(key[:2], deque(maxlen=7))
        lag_1 = history[-1] if history else 0
        rolling_mean = sum(history) / len(history) if history else 0.0
        result.append(
            {
                **row,
                "lag_1_units": str(lag_1),
                "rolling_7d_mean": f"{rolling_mean:.3f}",
                "baseline_next_day": f"{rolling_mean:.3f}",
            }
        )
        history.append(units)
    return result


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0]) if rows else []
    with path.open("w", newline="", encoding="utf-8") as target:
        writer = csv.DictWriter(target, fieldnames=fields)
        if fields:
            writer.writeheader()
            writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    rows = build_features(args.input)
    write_rows(args.output, rows)
    print(f"Built {len(rows)} feature rows at {args.output}")


if __name__ == "__main__":
    main()
