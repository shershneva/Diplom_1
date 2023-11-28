import pytest
from praktikum.bun import Bun


class TestBun:
    def test_get_name_correct_name(self):
        new_bun = Bun('Вкусная тестовая булочка', 555.6)
        assert new_bun.get_name() == 'Вкусная тестовая булочка'

    def test_get_price_correct_price(self):
        new_bun = Bun('Вкусная тестовая булочка', 555.6)
        assert new_bun.get_price() == 555.6
