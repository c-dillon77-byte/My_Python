#!/usr/bin/env python3
"""
Food cost calculator for two profit centers (Taco and Pizza).

Food cost uses the standard cost-of-goods-sold formula:

    COGS        = beginning inventory + purchases (receipts) - ending inventory
    Food cost % = COGS / total sales * 100

Run: python food_cost/food_cost.py
"""

from __future__ import annotations

from dataclasses import dataclass

PROFIT_CENTERS = ["Taco", "Pizza"]


@dataclass
class ProfitCenter:
    name: str
    beginning_inventory: float
    purchases: float
    ending_inventory: float
    sales: float

    @property
    def cogs(self) -> float:
        """Cost of goods sold = beginning + purchases - ending."""
        return self.beginning_inventory + self.purchases - self.ending_inventory

    @property
    def food_cost_pct(self) -> float:
        return food_cost_percent(self.cogs, self.sales)


def food_cost_percent(cogs: float, sales: float) -> float:
    """COGS as a percentage of sales (0 if there were no sales)."""
    return (cogs / sales) * 100 if sales else 0.0


def combine(centers: list[ProfitCenter]) -> tuple[float, float, float]:
    """Return (total COGS, total sales, combined food cost %)."""
    total_cogs = sum(c.cogs for c in centers)
    total_sales = sum(c.sales for c in centers)
    return total_cogs, total_sales, food_cost_percent(total_cogs, total_sales)


def ask_money(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).replace("$", "").replace(",", ""))
        except ValueError:
            print("Please enter a number, e.g. 1250.50")
            continue
        if value < 0:
            print("Please enter 0 or more.")
            continue
        return value


def ask_center(name: str) -> ProfitCenter:
    print(f"\n=== {name} Profit Center ===")
    return ProfitCenter(
        name=name,
        beginning_inventory=ask_money("Beginning Inventory: $"),
        purchases=ask_money("Purchases / Receipts: $"),
        ending_inventory=ask_money("Ending Inventory: $"),
        sales=ask_money("Total Sales: $"),
    )


def main() -> None:
    centers = [ask_center(name) for name in PROFIT_CENTERS]
    total_cogs, total_sales, total_pct = combine(centers)

    print("\n--- Food Cost Summary ---")
    for c in centers:
        print(f"{c.name + ' COGS:':<14}${c.cogs:,.2f} ({c.food_cost_pct:.2f}% of ${c.sales:,.2f} sales)")
    print("--------------------------------")
    print(f"Total COGS:   ${total_cogs:,.2f}")
    print(f"Total Sales:  ${total_sales:,.2f}")
    print(f"Combined Food Cost: {total_pct:.2f}%")


if __name__ == "__main__":
    main()
