# Customer Analytics Warehouse

## Problem
Turn raw order data into a tested analytics warehouse and then use it for segmentation and churn prediction.

## Dataset and provenance

`data/raw/customers.csv` and `orders.csv` are synthetic demo fixtures. For realistic analytics, download the [Olist Brazilian E-Commerce dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) or Online Retail II from its authorized source; observe the source terms and keep raw files under ignored `data/external/`.

### Download the Kaggle dataset

The downloader defaults to `olistbr/brazilian-ecommerce`. Install the Kaggle CLI with `python -m pip install kaggle`, create an API token in Kaggle account settings, and save `kaggle.json` to `%USERPROFILE%\.kaggle\kaggle.json` on Windows or `~/.kaggle/kaggle.json` on macOS/Linux. Run `python scripts/download_kaggle.py`; files go to ignored `data/external/`. Olist has multiple related CSV tables, so adapt/relate those tables to the warehouse inputs before loading. Review Kaggle's current license and terms; do not commit raw customer/order data.

## Run the ELT demo

From this directory, run `python src/main.py`. **Extract/load:** CSV snapshots are upserted into SQLite `raw_*` tables. **Transform in place:** SQL staging view casts and filters rows, then SQL aggregates a customer-sales mart. The transaction can be rerun safely; the generated `data/warehouse.sqlite` is ignored. For another source, supply `--data-dir` with `customers.csv` and `orders.csv` matching the fixture columns. Run `python -m pytest -q tests`.

## Stack
dbt, BigQuery/Snowflake/DuckDB, scikit-learn, BI

## Architecture
- Bronze / raw ingestion layer
- Silver / cleaned and validated data layer
- Gold / feature or serving layer
- Monitoring / validation and retraining feedback loop

## DE tasks
1. Ingest raw data with versioned file naming and timestamps.
2. Build idempotent and incremental transformations.
3. Add data quality checks and freshness alerts.
4. Create a reproducible run order using a Makefile or run script.
5. Store outputs in a warehouse, lake, or streaming sink with clear contracts.

## DS tasks
1. Run EDA and validate assumptions about seasonality, drift, and user behavior.
2. Benchmark a baseline model before trying a stronger approach.
3. Use proper time-based splits and avoid leakage.
4. Log experiments, tuning choices and key metrics.
5. Report limitations and next steps in a production-focused way.

## Deliverables
- Reproducible pipeline or app
- Tests for transformation and validation logic
- Dashboard, API, or report showing outputs
- Clear business summary with measurable impact

## Recommended repository structure
`	ext
customer-analytics-warehouse/
+-- README.md
+-- requirements.txt
+-- Makefile
+-- .gitignore
+-- src/
+-- tests/
+-- notebooks/
+-- docs/
`

## Resume line
Designed a tested star-schema warehouse in dbt and built RFM segmentation and churn models on top of it.
