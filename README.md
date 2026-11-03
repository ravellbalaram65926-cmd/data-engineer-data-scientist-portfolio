# Hybrid Data Engineer + Data Scientist Portfolio

This repository contains a structured starter kit for 8 hybrid portfolio projects tailored to data engineering + data science roles.

## Project catalog

| Project | Focus | Pipeline |
|---|---|---|
| [Retail Demand Forecasting](retail-demand-forecasting/README.md) | Store and item sales trends | ETL |
| [Real-Time Fraud Detection](real-time-fraud-detection/README.md) | Transaction validation and risk signals | ETL |
| [End-to-End MLOps Platform](end-to-end-mlops-platform/README.md) | Customer churn features for model training | ETL |
| [Customer Analytics Warehouse](customer-analytics-warehouse/README.md) | Customer and monthly sales marts | ELT |
| [RAG Document Search](rag-document-search-pipeline/README.md) | Document cleanup and search-ready chunks | ETL |
| [Recommendation Engine](recommendation-engine-at-scale/README.md) | User-item interaction aggregates | ELT |
| [IoT Energy Forecasting](iot-energy-demand-forecasting/README.md) | Meter readings and anomaly signals | ETL |
| [Data Quality Monitoring](data-quality-and-anomaly-monitoring/README.md) | Schema, completeness, and range checks | ETL |

Open a project above for its dataset, how to run it, and details of its flow.

## How to use
- Read each project README for its dataset, pipeline stages, and run instructions.
- Replace placeholder files with real pipelines, notebooks, and dashboards as you build each project.

## Local ETL / ELT demos

Each project includes a small synthetic sample dataset and an executable pipeline in `src/main.py`. From a project folder, run `python src/main.py`; run its tests with `python -m pytest -q tests`. To run all eight demos and tests, use `python scripts/run_portfolio.py` from the repository root (or add `--pipelines-only` / `--tests-only`). Outputs are reproducible and ignored by Git.

The sample fixtures are for workflow demonstrations, not real-world model evaluation. Project READMEs identify public dataset sources and access notes. Keep larger or access-controlled data in `data/external/`; that path is Git-ignored. Never commit secrets, personal data, or raw data whose terms do not allow redistribution.

### Using Kaggle datasets

Yes—Kaggle datasets can be used as inputs. Choose a dataset and review its license and Kaggle download terms first. To download private or gated datasets, configure Kaggle API credentials locally or as a repository/organization secret; never paste API tokens into chat or commit them. Place downloaded files under the project's ignored `data/external/` folder and point the pipeline at a compatible CSV file. Small synthetic samples remain available for demos and tests without Kaggle access.

## Automated quality and dependency checks

- **Portfolio CI** runs on pull requests, pushes to `main` or `master`, every Monday at 05:03 UTC, and manual dispatch. An eight-project matrix compiles, lints with Ruff, and runs each project's pytest suite. Dependency caching and concurrency cancellation keep repeat runs efficient.
- **Dependency audit** runs every Monday at 05:23 UTC or on manual dispatch. It audits each project's declared Python requirements with `pip-audit` and fails when known vulnerabilities are found.
- **Dependabot** checks Python dependencies in each project and GitHub Actions weekly. It groups minor and patch updates to reduce review noise; major updates remain separate.
- Both workflows use read-only repository permissions and do not publish artifacts or modify source files.

To reproduce the CI checks locally, install a project's `requirements.txt`, `pytest`, and `ruff`, then run:

```shell
python -m compileall PROJECT/src PROJECT/tests
python -m ruff check PROJECT/src PROJECT/tests
python -m pytest -q PROJECT/tests
```

Replace `PROJECT` with one of the project directory names above.

## Production-ready standards for each project
- Keep raw data out of git.
- Use reproducible setup files (`requirements.txt`, `Makefile`, environment config).
- Add tests for transformation logic.
- Include a business problem summary and quantified outcomes in the README.
- Add architecture diagrams and a limitations / next steps section.
