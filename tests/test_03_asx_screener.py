import pandas as pd
import pytest
from Exercises.ex03_asx_screener import screen_value_and_yield_stocks, add_score_and_rank


@pytest.fixture
def sample_df():
    return pd.DataFrame(
        [
            {"ticker": "BHP.AX", "name": "BHP Group", "sector": "Materials", "price": 42.5, "pe_ratio": 11.2, "dividend_yield": 5.8, "market_cap": 215.0},
            {"ticker": "CBA.AX", "name": "CommBank", "sector": "Financials", "price": 130.0, "pe_ratio": 22.4, "dividend_yield": 3.6, "market_cap": 218.0},
            {"ticker": "RIO.AX", "name": "Rio Tinto", "sector": "Materials", "price": 115.0, "pe_ratio": 10.5, "dividend_yield": 6.2, "market_cap": 42.0},
            {"ticker": "PENNY.AX", "name": "Penny Stock", "sector": "Energy", "price": 0.05, "pe_ratio": -5.0, "dividend_yield": 0.0, "market_cap": 0.02},
        ]
    )


def test_screen_value_and_yield_stocks(sample_df):
    screened = screen_value_and_yield_stocks(sample_df, min_dividend_yield=4.0, max_pe_ratio=20.0, min_market_cap_billions=1.0)
    assert len(screened) == 2
    # Expect RIO.AX (6.2%) first, then BHP.AX (5.8%)
    assert screened.iloc[0]["ticker"] == "RIO.AX"
    assert screened.iloc[1]["ticker"] == "BHP.AX"


def test_add_score_and_rank(sample_df):
    screened = screen_value_and_yield_stocks(sample_df, min_dividend_yield=4.0)
    ranked = add_score_and_rank(screened)

    assert "composite_score" in ranked.columns
    assert "rank" in ranked.columns
    assert ranked.iloc[0]["rank"] == 1
    # RIO score: (6.2 * 2) - 10.5 = 12.4 - 10.5 = 1.90
    assert ranked.iloc[0]["composite_score"] == 1.90
