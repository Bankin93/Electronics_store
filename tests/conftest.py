import pytest
from Product.product import Product, Phone, Keyboard


@pytest.fixture()
def item_class():
    item = Product("Смартфон", 10000, 20)
    return item


@pytest.fixture()
def phone_class():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    return phone


@pytest.fixture()
def keyboard_class():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb
