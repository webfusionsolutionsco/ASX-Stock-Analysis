"""
===============================================================================
EXERCISE 03: ASX Stock Screener using Pandas
===============================================================================
Level: Intermediate
Topic: Data Manipulation with Pandas DataFrames, Data Filtering & Ranking

BRIEF:
Yield and value investors screen the stock market to discover tickers that meet
specific financial metrics (e.g. high dividend yield, low P/E ratio, reasonable market cap).

In this exercise, you will write screening functions using `pandas` to filter a table
of ASX stock data and output ranked investment opportunities.

LEARNING GOALS:
  - Working with Pandas DataFrames (filtering, sorting, handling NaN values).
  - Boolean indexing with multi-criteria conditions (`&`, `|`).
  - Column derivations (creating new calculated columns).

INSTRUCTIONS:
  Complete the screening functions below where marked `# TODO`.
===============================================================================
"""

import pandas as pd


def screen_value_and_yield_stocks(
    df: pd.DataFrame,
    min_dividend_yield: float = 4.0,
    max_pe_ratio: float = 25.0,
    min_market_cap_billions: float = 1.0,
) -> pd.DataFrame:
    """
    Filters a DataFrame of stock metrics according to value & dividend yield criteria.

    Expected input DataFrame columns:
      - 'ticker': str (e.g., 'BHP.AX')
      - 'name': str
      - 'sector': str
      - 'price': float
      - 'pe_ratio': float
      - 'dividend_yield': float (as a percentage, e.g. 5.5 for 5.5%)
      - 'market_cap': float (in AUD billions, e.g. 120.5)

    Filter Conditions:
      1. 'dividend_yield' >= min_dividend_yield
      2. 'pe_ratio' > 0 and 'pe_ratio' <= max_pe_ratio (Ignore negative or zero P/E ratios)
      3. 'market_cap' >= min_market_cap_billions
      4. Drop any rows where 'ticker', 'price', 'pe_ratio', or 'dividend_yield' is NaN/missing.

    Sorting:
      Sort the resulting DataFrame by 'dividend_yield' descending, breaking ties with 'pe_ratio' ascending.

    Returns:
      Filtered and sorted DataFrame (with original index reset).
    """
    # TODO: Implement this function
    raise NotImplementedError("Complete screen_value_and_yield_stocks exercise function")


def add_score_and_rank(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates a simple custom composite score for each stock and ranks them.

    Composite Score Formula:
        Score = (dividend_yield * 2) - pe_ratio

    Higher dividend yields boost the score, while lower P/E ratios (cheaper valuation) increase the score.

    Actions:
      1. Create a new column named 'composite_score' calculated as: (dividend_yield * 2) - pe_ratio.
         Round 'composite_score' to 2 decimal places.
      2. Sort the DataFrame by 'composite_score' in descending order.
      3. Add a column named 'rank' starting from 1 for the highest score stock.
      4. Reset index (drop=True).

    Returns:
      DataFrame with 'composite_score' and 'rank' columns added.
    """
    # TODO: Implement this function
    raise NotImplementedError("Complete add_score_and_rank exercise function")


if __name__ == "__main__":
    print("--- Exercise 03 Demo ---")
    sample_data = pd.DataFrame(
        [
            {
                "ticker": "BHP.AX",
                "name": "BHP Group Ltd",
                "sector": "Materials",
                "price": 42.5,
                "pe_ratio": 11.2,
                "dividend_yield": 5.8,
                "market_cap": 215.0,
            },
            {
                "ticker": "CBA.AX",
                "name": "Commonwealth Bank",
                "sector": "Financials",
                "price": 130.0,
                "pe_ratio": 22.4,
                "dividend_yield": 3.6,
                "market_cap": 218.0,
            },
            {
                "ticker": "WTC.AX",
                "name": "WiseTech Global",
                "sector": "Technology",
                "price": 95.0,
                "pe_ratio": 85.0,
                "dividend_yield": 0.2,
                "market_cap": 31.0,
            },
            {
                "ticker": "RIO.AX",
                "name": "Rio Tinto Ltd",
                "sector": "Materials",
                "price": 115.0,
                "pe_ratio": 10.5,
                "dividend_yield": 6.2,
                "market_cap": 42.0,
            },
            {
                "ticker": "PENNY.AX",
                "name": "Micro Speculator",
                "sector": "Energy",
                "price": 0.05,
                "pe_ratio": -5.0,
                "dividend_yield": 0.0,
                "market_cap": 0.02,
            },
        ]
    )

    try:
        screened = screen_value_and_yield_stocks(sample_data)
        ranked = add_score_and_rank(screened)
        print("Screened & Ranked Results:\n", ranked[["rank", "ticker", "dividend_yield", "pe_ratio", "composite_score"]])
    except NotImplementedError as e:
        print(f"Function not implemented yet: {e}")
