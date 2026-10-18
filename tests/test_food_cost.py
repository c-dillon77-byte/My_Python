import pytest

from food_cost.food_cost import ProfitCenter, combine, food_cost_percent


def test_cogs_includes_ending_inventory():
    c = ProfitCenter("Taco", beginning_inventory=1000, purchases=500, ending_inventory=300, sales=4000)
    assert c.cogs == pytest.approx(1200)  # 1000 + 500 - 300
    assert c.food_cost_pct == pytest.approx(30.0)


def test_zero_sales_does_not_crash():
    assert food_cost_percent(100, 0) == 0.0


def test_combined_totals():
    taco = ProfitCenter("Taco", 1000, 500, 300, 4000)  # COGS 1200
    pizza = ProfitCenter("Pizza", 800, 400, 200, 3000)  # COGS 1000
    total_cogs, total_sales, pct = combine([taco, pizza])
    assert total_cogs == pytest.approx(2200)
    assert total_sales == pytest.approx(7000)
    assert pct == pytest.approx(2200 / 7000 * 100)
