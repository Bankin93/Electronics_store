import pytest
from Product.product import Product


def test_instantiate_from_csv():
    Product.instantiate_from_csv('test.csv')
    assert len(Product.product_list) == 5
    assert Product.product_list[3].name == "Мышка"
    assert Product.product_list[2].price == 10
    assert Product.product_list[0].quantity == 1


@pytest.fixture()
def item_class():
    item = Product("Смартфон", 10000, 20)
    return item


def test_repr(item_class):
    assert repr(item_class) == "Product('Смартфон', 10000, 20)"


def test_str(item_class):
    assert str(item_class) == "Смартфон"


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


@pytest.fixture()
def product_name():
    return Product.product_list


def test_name(product_name):
    with pytest.raises(Exception):
        product_name.name = 'Длина наименования товара превышает 10 символов.'


def test_is_integer():
    assert Product.is_integer(5) is True
    assert Product.is_integer(5.0) is True
    assert Product.is_integer(5.5) is False
