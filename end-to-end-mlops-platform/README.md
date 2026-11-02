# End-to-End MLOps Platform

## Problem
Train, deploy and monitor a customer churn model in a repeatable, automated workflow.

## Data
Telco Customer Churn

## Stack
Airflow, MLflow, Docker, FastAPI, GitHub Actions, Evidently

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
end-to-end-mlops-platform/
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
Built an automated training-to-serving MLOps pipeline with CI/CD, model registry and drift monitoring.
