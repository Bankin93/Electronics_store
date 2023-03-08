import os

import pytest
from product.product import Product, Phone, Keyboard

@pytest.fixture()
def test_file():
    test_file = os.path.join("csv_files/test.csv")
    return test_file

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


@pytest.fixture()
def error_file():
    error_file = os.path.join("csv_files/error.csv")
    return error_file


@pytest.fixture()
def missing_file():
    missing_file = os.path.join("missing.csv")
    return missing_file

