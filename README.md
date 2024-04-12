# Portafolio

A simple Python project to calculate the profit and annualized profit for a given financial dataset.

## Description

This project aims to calculate the profit and annualized profit for a given financial dataset using Python. It utilizes the yfinance library to fetch historical stock data and the pandas library for data manipulation and analysis. The project is designed to be used within a virtual environment to ensure package isolation and reproducibility.

## Features

- Fetch historical stock data using yfinance
- Calculate profit based on the stock data
- Calculate annualized profit based on the stock data
- Utilize virtual environments for package isolation

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/vicente999/profit_calculator.git
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # for Linux/Mac
    venv\Scripts\activate  # for Windows
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:

    ```bash
    python main.py
    ```

2. Variables of the proyect can be modified in the main.py file, for example:

    ```python
    etf_symbol = 'SPY'
    start_date = '2020-01-01'
    end_date = '2024-01-01'

    profit_start_date = '2020-01-02'
    profit_end_date = '2021-01-29'

    annualized_profit_start_date = '2020-01-02'
    annualized_profit_end_date = '2021-01-29'
    ```
