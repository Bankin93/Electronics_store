import pytest
from product.exeption import InstantiateCSVError
from product.product import Product


def test_instantiate_from_csv(test_file):
    Product.instantiate_from_csv(path=test_file)
    product_1 = Product.product_list[0]
    product_2 = Product.product_list[1]
    product_3 = Product.product_list[2]
    product_4 = Product.product_list[3]

    assert len(Product.product_list) == 4
    assert product_4.name == "Мышка"
    assert product_3.price == 10.0
    assert product_1.quantity == 1
    assert product_2.name == "Геймпад"


def test_instantiate_from_csv_missing(missing_file):
    assert Product.instantiate_from_csv(path=missing_file) == f'Отсутствует файл {missing_file}'


def test_instantiate_from_csv_error(error_file):
    assert Product.instantiate_from_csv(path=error_file) == f'Файл {error_file} поврежден'


def test_repr(item_class):
    assert repr(item_class) == "Product('Смартфон', 10000, 20)"


def test_str(item_class):
    assert str(item_class) == "Смартфон"


def test_name(item_class):
    item_class.name = "Наушники"
    assert item_class.name == "Наушники"
    with pytest.raises(Exception):
        item_class.name = 'Длина наименования товара превышает 10 символов.'


def test_is_integer():
    assert Product.is_integer(5) is True
    assert Product.is_integer(5.0) is True
    assert Product.is_integer(5.5) is False


def test_calculate_total_price(item_class):
    assert item_class.calculate_total_price() == 200000


def test_apply_discount(item_class):
    Product.discount = 0.8
    assert item_class.price == 10000
    assert item_class.apply_discount() == 8000.0


def test_instantiate_csv_error():
    e = InstantiateCSVError()
    assert (str(e)) == "Неизвестная ошибка"
