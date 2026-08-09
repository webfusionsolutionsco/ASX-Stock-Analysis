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

from typing import List, Dict, Any, Optional
from dataclasses import dataclass


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
    # TODO: Implement this function
    raise NotImplementedError("Complete clean_and_parse_quotes exercise function")


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
    # TODO: Implement this function
    raise NotImplementedError("Complete calculate_daily_returns exercise function")


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
    # TODO: Implement this function
    raise NotImplementedError("Complete calculate_sma exercise function")


if __name__ == "__main__":
    print("--- Exercise 01 Demo ---")
    raw_data = [
        {"ticker": "bhp.ax", "date": "2026-08-01", "close_price": 40.0, "volume": 1000000},
        {"ticker": "BHP.AX", "date": "2026-08-02", "close_price": 42.0, "volume": 1200000},
        {"ticker": "BHP.AX", "date": "2026-08-03", "close_price": 41.1, "volume": 900000},
        {"ticker": "INVALID", "date": "2026-08-04", "close_price": -10.0, "volume": 0},
    ]
    try:
        cleaned = clean_and_parse_quotes(raw_data)
        print(f"Cleaned Quotes ({len(cleaned)}):", cleaned)
    except NotImplementedError as e:
        print(f"Function not implemented yet: {e}")
