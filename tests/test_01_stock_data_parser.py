import pytest
from Exercises.ex01_stock_data_parser import (
    StockQuote,
    clean_and_parse_quotes,
    calculate_daily_returns,
    calculate_sma,
)


def test_clean_and_parse_quotes():
    raw_data = [
        {"ticker": "bhp.ax", "date": "2026-08-01", "close_price": 40.0, "volume": 1000000},
        {"ticker": "cba.ax", "date": "2026-08-01", "close_price": -5.0, "volume": 500000},  # Invalid price
        {"ticker": "", "date": "2026-08-01", "close_price": 10.0, "volume": 100},  # Empty ticker
        {"ticker": "WES.AX", "date": "2026-08-01", "close_price": 65.0, "volume": 300000},
    ]

    result = clean_and_parse_quotes(raw_data)
    assert len(result) == 2
    assert result[0].ticker == "BHP.AX"
    assert result[0].close_price == 40.0
    assert result[1].ticker == "WES.AX"


def test_calculate_daily_returns():
    prices = [100.0, 105.0, 102.9]
    returns = calculate_daily_returns(prices)
    assert returns == [5.0, -2.0]

    # Less than 2 prices should yield empty list
    assert calculate_daily_returns([50.0]) == []


def test_calculate_sma():
    prices = [10.0, 12.0, 14.0, 16.0, 18.0]
    sma3 = calculate_sma(prices, window=3)
    assert sma3 == [None, None, 12.0, 14.0, 16.0]

    with pytest.raises(ValueError):
        calculate_sma(prices, window=0)
