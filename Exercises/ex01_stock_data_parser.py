"""
===============================================================================
EXERCISE 01: ASX Stock Data Parser & Financial Metrics Calculation
===============================================================================
Level: Intermediate
Topic: Data Structures, Type Hints, Exception Handling & Algorithmic Math

BRIEF:
When building a production-ready stock analysis tool, raw data from APIs (like Yahoo Finance
or ASX market feeds) often comes in messy or unformatted structures. Your job in this exercise
is to implement functions that parse raw ASX price records, clean out invalid records, and compute
key financial statistics:
  1. Parse raw price dictionary entries into structured dictionaries or dataclasses.
  2. Compute Daily Returns (%) across a time series of closing prices.
  3. Calculate an N-day Simple Moving Average (SMA).

LEARNING GOALS:
  - Working with list comprehensions and clean error handling.
  - Using type hints (`List[float]`, `Dict[str, Any]`, `Optional[float]`).
  - Edge case handling (e.g. empty lists, division by zero, invalid numbers).

INSTRUCTIONS:
  Complete the function stubs below where marked `# TODO`. Run `pytest` in your terminal to test!
===============================================================================
"""

import pandas as pd

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import date

@dataclass
class StockQuote:
    ticker: str
    date: str
    close_price: float
    volume: int


def clean_and_parse_quotes(raw_quotes: List[Dict[str, Any]]) -> List[StockQuote]:
    """
    Parses a list of raw dictionary quotes and filters out invalid records.

    Rules:
      - Ticker must be a non-empty string and converted to uppercase (e.g., 'bhp.ax' -> 'BHP.AX').
      - close_price must be a positive float (> 0). If it is <= 0 or missing/invalid type, skip the record.
      - volume must be an integer >= 0. If missing or invalid, skip the record.
      - date must be a non-empty string.

    Args:
        raw_quotes: List of dictionaries containing raw stock data.

    Returns:
        List of valid StockQuote instances.

    Example input:
        [
            {"ticker": "bhp.ax", "date": "2026-08-01", "close_price": 42.50, "volume": 1200000},
            {"ticker": "cba.ax", "date": "2026-08-01", "close_price": -5.00, "volume": 500000},  # Invalid price!
        ]
    """
    def is_valid_iso_date(date_str: str) -> bool:
        if not isinstance(date_str, str):
            return False
        try:
            date.fromisoformat(date_str.strip())
            return True
        except (ValueError, TypeError):
            return False

    def parse_quote(raw_quote: Dict[str, Any]) -> Optional[StockQuote]:
        # Ensure validated keys are present in quote
        expected_keys = {"ticker", "date", "close_price", "volume"}
        if not expected_keys.issubset(raw_quote.keys()):
            print(f"Missing required keys: {expected_keys - raw_quote.keys()}")
            return None

        # Validate:
        # Ticker - non empty string, convert to upper case
        valid_ticker = (
            isinstance(raw_quote["ticker"], str)
            and bool(raw_quote["ticker"].strip())
        )
        # Close price - positive float
        valid_close_price =  (
            isinstance(raw_quote["close_price"], float) 
            and not isinstance(raw_quote["close_price"], bool) 
            and raw_quote["close_price"] > 0
        )
        # Volume - natural number
        valid_volume = (
            isinstance(raw_quote["volume"], int)
            and raw_quote["volume"] >= 0
        )
        # Date - is valid date
        valid_date = is_valid_iso_date(raw_quote["date"])
        if (valid_ticker and valid_close_price and valid_volume and valid_date):
            return StockQuote(
                ticker = raw_quote["ticker"].upper(),
                date = raw_quote["date"],
                close_price = raw_quote["close_price"],
                volume = raw_quote["volume"]
            )

    return [validated_quote for quote in raw_quotes if (validated_quote := parse_quote(quote))]

def calculate_daily_returns(prices: List[float]) -> List[float]:
    """
    Calculates percentage daily returns from a list of sequential closing prices.
    
    Formula:
        Daily Return (%) = ((Price_t - Price_{t-1}) / Price_{t-1}) * 100

    Args:
        prices: List of closing prices ordered from oldest to newest.

    Returns:
        List of daily return percentages rounded to 2 decimal places.
        Note: The returned list will have length = len(prices) - 1.
        If len(prices) < 2, return an empty list.

    Example:
        prices = [100.0, 105.0, 102.9]
        returns = [5.0, -2.0]
    """
    # Function to calculate percentage return given 2 prices in sequential order
    def calculate_return(price_a: float, price_b: float):
        return round(((price_b - price_a) / price_a) * 100, 2)

    if (len(prices) <= 2):
        return []
    else: 
        return [calculate_return(price_a, price_b) for price_a, price_b in zip(prices, prices[1:])]

def calculate_sma(prices: List[float], window: int) -> List[Optional[float]]:
    """
    Calculates the Simple Moving Average (SMA) over a specified rolling window.

    Args:
        prices: List of closing prices.
        window: The moving average window size (e.g., 5-day SMA).

    Returns:
        List of SMA values matching the length of `prices`.
        For indices where there are fewer than `window` prices available, the value should be `None`.
        Each calculated SMA value should be rounded to 2 decimal places.

    Raises:
        ValueError: If window is less than 1.

    Example:
        prices = [10.0, 12.0, 14.0, 16.0, 18.0], window = 3
        Returns: [None, None, 12.0, 14.0, 16.0]
    """
    if (window < 1):
        raise ValueError
        
    prices_dict = {'value': prices}
    # Assign pandas dataframe for rolling and mean methods
    prices_df = pd.DataFrame(prices_dict)
    # Assign to series
    sma_series = prices_df['value'].rolling(window).mean()
    # Replace Nan with None, and convert to list for return
    return sma_series.astype(object).fillna(None).tolist()

if __name__ == "__main__":
    print("--- Exercise 01 Demo ---")
    raw_data_cleaned = [
        {"ticker": "bhp.ax", "date": "2026-08-01", "close_price": 40.0, "volume": 1000000},
        {"ticker": "BHP.AX", "date": "2026-08-02", "close_price": 42.0, "volume": 1200000},
        {"ticker": "BHP.AX", "date": "2026-08-03", "close_price": 41.1, "volume": 900000},
        {"ticker": "INVALID", "date": "2026-08-04", "close_price": -10.0, "volume": 0},
    ]
    raw_data_returns = [100.0, 105.0, 102.9, 110.2, 112.4, 108.68]
    raw_data_prices = [10.0, 12.0, 14.0, 16.0, 18.0]
    averages_window = 3
    try:
        cleaned = clean_and_parse_quotes(raw_data_cleaned)
        print(f"Cleaned Quotes ({len(cleaned)}):", cleaned)
        returns = calculate_daily_returns(raw_data_returns)
        print(f"Daily returns {returns}")
        averages = calculate_sma(raw_data_prices, averages_window)
        print(f"Simple moving averages: {averages}")
    except NotImplementedError as e:
        print(f"Function not implemented yet: {e}")
