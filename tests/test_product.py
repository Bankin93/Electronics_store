import pytest
from Product.Product import Product


@pytest.mark.parametrize(
    "name, price, quantity, result",
    [("Смартфон", 10000, 20, 200000), ("Ноутбук", 20000, 5, 100000)]
)
def test_calculate_total_price(name, price, quantity, result):
    item = Product(name, price, quantity)
    assert item.calculate_total_price() == result


@pytest.mark.parametrize(
    "name, price, quantity, result",
    [("Смартфон", 10000, 20, 8000.0), ("Ноутбук", 20000, 5, 16000.0)]
)
def test_apply_discount(name, price, quantity, result):
    Product.discount = 0.8
    item = Product(name, price, quantity)
    assert item.price == price
    assert item.apply_discount() == result
