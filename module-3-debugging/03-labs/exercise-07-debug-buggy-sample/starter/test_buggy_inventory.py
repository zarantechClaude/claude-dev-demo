# TEACHING ARTEFACT - test suite for Exercise 7. Do not change the tests.
# They are the specification. If a test looks wrong, read it again.
import pytest
from buggy_inventory import restock, reorder_quantity


def test_restock_applies_deliveries():
    inv = {"widget": 2, "bolt": 10}
    out = restock(inv, [{"sku": "widget", "qty": 5}])
    assert inv["widget"] == 7
    assert out == []


def test_restock_flags_low_items():
    inv = {"widget": 1, "bolt": 40}
    out = restock(inv, [])
    assert out == ["widget"]


def test_reorder_covers_shortfall():
    # current 7, threshold 20, packs of 5 -> shortfall 13 -> need 3 packs
    assert reorder_quantity(7, 20, 5) == 3
