# Customer Analytics Warehouse

## Problem
Turn raw order data into a tested analytics warehouse and then use it for segmentation and churn prediction.

## Data
Olist or Online Retail II

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
+-- .github/workflows/ci.yml
`

## Resume line
Designed a tested star-schema warehouse in dbt and built RFM segmentation and churn models on top of it.
