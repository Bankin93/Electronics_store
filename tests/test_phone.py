import pytest


def test_str(phone_class):
    assert str(phone_class) == "iPhone 14"


def test_repr(phone_class):
    assert repr(phone_class) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(phone_class):
    assert phone_class.number_of_sim == 2
    phone_class.number_of_sim = 1
    assert phone_class.number_of_sim == 1
    with pytest.raises(Exception):
        phone_class.number_of_sim = 0


def test_add(item_class, phone_class):
    assert item_class + phone_class == 25
    assert phone_class + item_class == 25
    assert phone_class + phone_class == 10
    assert item_class + item_class == 40
    with pytest.raises(ValueError):
        print(phone_class + 7)
