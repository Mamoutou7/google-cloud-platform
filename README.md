# google-cloud-platform

A concise learning repository for Google Cloud and applied machine learning.

## Overview

This project collects educational material around:
- **BigQuery** Python examples (`bigquery-scripts/`)
- **Keras feature engineering** notebooks (`keras-feature-engineering/`)
- **Course slides and reference PDFs** (`lectures/`)
- **Sample BigQuery resources** (`bigquery/resources-names/`)

It is best suited for experimentation, study, and quick demos rather than as a production application.

## Project Structure

```text
.
├── bigquery-scripts/            # Small BigQuery Python examples
├── bigquery/
│   └── resources-names/         # Sample USA names files
├── keras-feature-engineering/   # Notebooks + requirements
└── lectures/                    # Course PDFs and slides
```

## Requirements

- Python 3.8+
- A Google Cloud project with BigQuery enabled
- Google Cloud authentication configured locally

For the Keras notebooks:

```bash
pip install -r keras-feature-engineering/requirements.txt
```

## Usage

Run a BigQuery example:

```bash
python bigquery-scripts/client_query.py
```

Open the notebooks:

```bash
jupyter notebook keras-feature-engineering/
```

## Notes

- Most BigQuery scripts assume valid Google Cloud credentials are already available.
- The repository contains standalone scripts and notebooks, not a single packaged application.
- Large data samples and lecture documents are included for learning purposes.

## License

This project includes a `LICENSE` file at the repository root.
