# Retail Demand Forecasting Pipeline

## Problem
Forecast the next 28 days of unit sales per item and store from an automatically refreshing pipeline.

## Data
M5 Forecasting (Walmart) dataset

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
+-- .github/workflows/ci.yml
`

## Resume line
Built a medallion-architecture forecasting pipeline that reduced MAPE versus a seasonal-naive baseline while automating refresh and experiment tracking.
