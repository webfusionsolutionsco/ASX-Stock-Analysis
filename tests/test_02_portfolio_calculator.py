import pytest
from Exercises.ex02_portfolio_calculator import PortfolioTracker


def test_portfolio_tracker():
    portfolio = PortfolioTracker()
    portfolio.add_or_update_position("BHP.AX", shares=100, purchase_price=40.0, current_price=50.0, dividend_yield_pct=5.0)
    portfolio.add_or_update_position("CBA.AX", shares=50, purchase_price=100.0, current_price=100.0, dividend_yield_pct=3.0)

    # BHP market val: 100 * 50 = $5000 (cost 4000)
    # CBA market val: 50 * 100 = $5000 (cost 5000)
    # Total cost = 9000, Total market val = 10000

    assert portfolio.total_cost_basis() == 9000.0
    assert portfolio.total_market_value() == 10000.0

    pnl = portfolio.total_unrealized_pnl()
    assert pnl["amount"] == 1000.0
    assert pytest.approx(pnl["percentage"], 0.01) == 11.11

    weights = portfolio.get_position_weights()
    assert weights["BHP.AX"] == 50.0
    assert weights["CBA.AX"] == 50.0

    # Weighted yield: (50% * 5.0%) + (50% * 3.0%) = 4.0%
    assert portfolio.weighted_dividend_yield() == 4.0
