import pytest

from cash_register.cash_register import Item, line_item, totals


def test_item_with_percent_discount_and_tax():
    it = Item(name="Burger", qty=2, unit_price=5.00, tax_rate=0.07, discount_type="PCT", discount_value=10)
    assert it.gross == pytest.approx(10.00)
    assert it.discount_amount == pytest.approx(1.00)
    assert it.net == pytest.approx(9.00)
    assert it.tax == pytest.approx(0.63)
    assert it.total == pytest.approx(9.63)


def test_fixed_discount_cannot_exceed_price():
    it = Item(name="Soda", qty=1, unit_price=1.50, tax_rate=0.0, discount_type="AMT", discount_value=5)
    assert it.discount_amount == pytest.approx(1.50)
    assert it.total == pytest.approx(0.0)


def test_totals_add_up():
    items = [
        Item("A", 1, 10.00, 0.07),
        Item("B", 3, 2.00, 0.00),
    ]
    t = totals(items)
    assert t["net"] == pytest.approx(16.00)
    assert t["tax"] == pytest.approx(0.70)
    assert t["total"] == pytest.approx(16.70)


def test_line_item_is_receipt_width():
    assert len(line_item("SUBTOTAL", "$16.00")) == 42
