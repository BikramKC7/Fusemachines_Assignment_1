# aifellowship12factor

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

simple proejct on cookiecutter

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         aifellowship12factor and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── aifellowship12factor   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes aifellowship12factor a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations



# 💱 Currency Converter API

A lightweight and fast **Currency Converter** application built with **FastAPI**. This API allows you to convert amounts from one currency to another using real-time or fixed exchange rates.

---

## 🚀 Features

- Convert between major international currencies
- FastAPI-powered web backend for high performance
- RESTful API endpoints
- Dockerized for easy deployment

---

## 🛠 How to Run the Project

### 🔹 Option 1: Run Locally

1. **Clone the repository**:

   ```bash
   git clone https://github.com/bikramkc7/currency-converter.git
   cd currency-converter


Create and activate a virtual environment:

python -m venv env

source env/bin/activate  # On Windows: env\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run the FastAPI app:
uvicorn main:app --reload


Access the API:

Visit http://127.0.0.1:8000

Interactive docs at http://127.0.0.1:8000/docs


🔹 Option 2: Run with Docker

Build and run using Docker:
    docker build -t currency-converter .
    docker run -d -p 8000:8000 currency-converter

Or use Docker Compose (if provided):
    docker-compose up --build

Visit in your browser:

    API: http://localhost:8000

    Docs: http://localhost:8000/docs


⚙️ Configuration Notes
The default port is 8000

If the app uses real-time exchange APIs (e.g., fixer.io or exchangerate.host), you might need to:

    Add an API key as an environment variable or in a .env file

    Example: EXCHANGE_API_KEY=your_api_key

Environment variables can be managed in a .env file or passed in the Docker container.





