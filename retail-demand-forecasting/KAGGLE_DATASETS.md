# Kaggle dataset setup

The optional downloader defaults to the [M5 Forecasting competition](https://www.kaggle.com/competitions/m5-forecasting-accuracy/data). M5 is large and requires accepting the competition rules on Kaggle.

1. Install the Kaggle CLI: `python -m pip install kaggle`.
2. Create an API token in Kaggle account settings. Save `kaggle.json` to `%USERPROFILE%\.kaggle\kaggle.json` on Windows or `~/.kaggle/kaggle.json` on macOS/Linux. Create the `.kaggle` folder if it does not exist. Never share or commit this file.
3. From this repository, run `python scripts/download_kaggle.py`.

The archive is extracted under `data/external/`, which is ignored by Git. This project’s pipeline expects a processed input schema; the M5 wide sales table must be adapted before use. The download script does not add raw Kaggle files to GitHub.
