import pytest


def test_change_lang(keyboard_class):
    assert keyboard_class.language == 'EN'
    keyboard_class.change_lang()
    assert keyboard_class.language == 'RU'
    keyboard_class.change_lang()
    assert keyboard_class.language == 'EN'
    with pytest.raises(AttributeError):
        keyboard_class.language = 'CH'
