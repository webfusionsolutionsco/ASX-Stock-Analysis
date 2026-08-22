"""
===============================================================================
EXERCISE 02: ASX Portfolio Valuation & Yield Aggregator
===============================================================================
Level: Intermediate
Topic: Classes, Dictionaries, Aggregations & Financial Mathematics

BRIEF:
Managing an ASX portfolio requires tracking holding positions, cost bases, market values,
and dividend yields across multiple shares (e.g. CBA.AX, BHP.AX, WES.AX, TLS.AX).

In this exercise, you will create a `PortfolioTracker` class that can:
  1. Add/modify stock positions with purchase price and current market price.
  2. Compute total portfolio current market value and total cost basis.
  3. Compute total unrealized profit/loss ($ and %).
  4. Compute individual position weightings (% of total portfolio).
  5. Compute the portfolio's overall weighted average dividend yield.

LEARNING GOALS:
  - Object-Oriented Programming (OOP) in Python.
  - State management inside standard classes.
  - Aggregating financial statistics safely without zero-division crashes.

INSTRUCTIONS:
  Complete the class methods below where marked `# TODO`.
===============================================================================
"""

from typing import Dict, Any


class PortfolioTracker:
    def __init__(self):
        """
        Initializes an empty portfolio.
        Store holdings in a dictionary structure such as:
        self.holdings = {
            "BHP.AX": {"shares": 100, "purchase_price": 40.0, "current_price": 45.0, "dividend_yield_pct": 5.2},
            ...
        }
        """
        self.holdings: Dict[str, Dict[str, Any]] = {}

    def add_or_update_position(
        self, ticker: str, shares: int, purchase_price: float, current_price: float, dividend_yield_pct: float = 0.0
    ) -> None:
        """
        Adds a new stock position or updates an existing position.

        Args:
            ticker: Ticker symbol (e.g. 'CBA.AX'). Should be capitalized.
            shares: Number of shares owned (must be > 0).
            purchase_price: Average purchase cost per share (must be > 0).
            current_price: Current market price per share (must be > 0).
            dividend_yield_pct: Annual dividend yield percentage (e.g. 4.5 for 4.5%). Default is 0.0.

        Raises:
            ValueError: If shares <= 0, purchase_price <= 0, or current_price <= 0.
        """
        if (shares <= 0 or purchase_price <= 0 or current_price <= 0):
            raise ValueError("Shares and prices must be greater than 0")

        holding = {
            "shares": shares,
            "purchase_price": purchase_price,
            "current_price": current_price,
            "dividend_yield_pct": dividend_yield_pct
        }

        if (ticker in self.holdings.keys()):
            print(f"Ticker {ticker.upper()} exists, updating")
        else:
            print(f"Adding ticker {ticker}")

        self.holdings[ticker] = holding

    def total_cost_basis(self) -> float:
        """
        Calculates the total purchase cost of all active holdings.
        Total Cost = sum(shares * purchase_price) across all positions.

        Returns:
            Total cost rounded to 2 decimal places.
        """

        return round(sum(holding["shares"] * holding["purchase_price"] for holding in self.holdings.values()), 2)

    def total_market_value(self) -> float:
        """
        Calculates the total current market value of all active holdings.
        Total Value = sum(shares * current_price) across all positions.

        Returns:
            Total market value rounded to 2 decimal places.
        """
        return round(sum(holding["shares"] * holding["current_price"] for holding in self.holdings.values()), 2)

    def total_unrealized_pnl(self) -> Dict[str, float]:
        """
        Calculates the overall portfolio profit/loss.

        Returns:
            A dictionary with:
              - "amount": Dollar profit or loss (total_market_value - total_cost_basis), rounded to 2 decimals.
              - "percentage": Percentage return ((total_market_value - total_cost_basis) / total_cost_basis) * 100, rounded to 2 decimals.
              If cost basis is 0.0, return percentage 0.0.
        """
        total_market_value = self.total_market_value()
        total_cost_basis = self.total_cost_basis()
        pnl = {
            "amount": round(total_market_value - total_cost_basis, 2),
            "percentage": round(((total_market_value - total_cost_basis) / total_cost_basis) * 100, 2)
        }
        return pnl

    def get_position_weights(self) -> Dict[str, float]:
        """
        Calculates each position's percentage weight relative to total market value.

        Returns:
            Dictionary mapping ticker to market value percentage (e.g., {"BHP.AX": 60.0, "CBA.AX": 40.0}).
            Each weight should be rounded to 2 decimal places.
            If total market value is 0.0, return an empty dictionary.
        """
        total_market_value = self.total_market_value()

        def calculate_weight(shares: int, current_price: float):
            return round(((shares * current_price) / total_market_value) * 100, 2)
        return {ticker: calculate_weight(holding["shares"], holding["current_price"]) for ticker, holding in self.holdings.items()}

    def weighted_dividend_yield(self) -> float:
        """
        Calculates the weighted average dividend yield (%) of the entire portfolio based on current market values.

        Formula:
            Weighted Yield = sum(position_weight * position_dividend_yield_pct) / 100  [if weights are in %]
            Or: sum(position_market_value * dividend_yield_pct) / total_market_value

        Returns:
            Weighted dividend yield rounded to 2 decimal places.
            If total market value is 0.0, return 0.0.
        """
        position_weights = self.get_position_weights()
        total_market_value = self.total_market_value()
        if (total_market_value == 0.0):
            return 0.0

        return round(sum(position_weights[ticker] * holding["dividend_yield_pct"] for ticker, holding in self.holdings.items()) / 100, 2)


if __name__ == "__main__":
    print("--- Exercise 02 Demo ---")
    portfolio = PortfolioTracker()
    try:
        portfolio.add_or_update_position("BHP.AX", shares=100, purchase_price=40.0, current_price=44.0, dividend_yield_pct=5.5)
        portfolio.add_or_update_position("CBA.AX", shares=50, purchase_price=100.0, current_price=120.0, dividend_yield_pct=3.8)
        print("Total Cost Basis: $", portfolio.total_cost_basis())
        print("Total Market Value: $", portfolio.total_market_value())
        print("Unrealized P&L:", portfolio.total_unrealized_pnl())
        print("Position Weights:", portfolio.get_position_weights())
        print("Weighted Yield:", portfolio.weighted_dividend_yield(), "%")
    except NotImplementedError as e:
        print(f"Function not implemented yet: {e}")
