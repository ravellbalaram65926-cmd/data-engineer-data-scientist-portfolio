import unittest
from pathlib import Path

from src.main import build_features


class RetailPipelineTests(unittest.TestCase):
    def test_features_use_only_prior_observations(self):
        sample = Path(__file__).resolve().parents[1] / "data/raw/sample_sales.csv"
        rows = build_features(sample)
        first_item = [row for row in rows if row["item_id"] == "ITEM-A"]
        self.assertEqual(first_item[0]["rolling_7d_mean"], "0.000")
        self.assertEqual(first_item[1]["lag_1_units"], "10")
        self.assertEqual(first_item[1]["rolling_7d_mean"], "10.000")

    def test_duplicate_daily_keys_are_idempotent(self):
        sample = Path(__file__).resolve().parents[1] / "data/raw/sample_sales.csv"
        rows = build_features(sample)
        keys = {(row["store_id"], row["item_id"], row["date"]) for row in rows}
        self.assertEqual(len(keys), len(rows))


if __name__ == "__main__":
    unittest.main()
