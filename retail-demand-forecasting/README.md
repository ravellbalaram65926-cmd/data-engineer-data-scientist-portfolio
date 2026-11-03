# Retail Demand Forecasting Pipeline

## Problem
Forecast the next 28 days of unit sales per item and store from an automatically refreshing pipeline.

## Dataset and provenance

- The committed `data/raw/sample_sales.csv` is a tiny synthetic fixture for tests and the local demo; it contains no Walmart data.
- For realistic experiments, download the M5 competition data from [Kaggle](https://www.kaggle.com/competitions/m5-forecasting-accuracy/data). Kaggle authentication and competition rules apply. Keep downloaded files under `data/external/` (ignored by Git) and adapt the input schema; do not commit raw files.

### Download M5 from Kaggle

Install the Kaggle CLI with `python -m pip install kaggle`. Create an API token in Kaggle account settings and save `kaggle.json` to `%USERPROFILE%\.kaggle\kaggle.json` on Windows or `~/.kaggle/kaggle.json` on macOS/Linux. Accept the competition rules on Kaggle, then run `python scripts/download_kaggle.py`. Files are extracted into ignored `data/external/`; the M5 files are large. The demo pipeline still uses its sample CSV; adapt the M5 wide sales table to the demo input schema before running against it.

## Run the ETL demo

From this directory, run `python src/main.py`. It validates and sorts source rows, deduplicates `(store_id, item_id, date)`, and writes lag-1, prior-seven-observation mean, and a simple baseline to `data/gold/forecast_features.csv`. Output is deterministic and safely regenerable.

The flow is **extract** CSV, **transform**/validate and build features, then **load** the gold CSV. Try `python src/main.py --input data/external/your_sales.csv --output data/gold/features.csv` after matching the demo schema.

Run checks from this directory with `python -m pytest -q tests`.

## Stack
PySpark, Delta Lake, MLflow, LightGBM, Prophet, Streamlit

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
retail-demand-forecasting/
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
Built a medallion-architecture forecasting pipeline that reduced MAPE versus a seasonal-naive baseline while automating refresh and experiment tracking.
