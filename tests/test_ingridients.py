import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:
    def test_get_price_correct_price(self):
        new_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Тестовый', 77)
        assert new_ingredient.get_price() == 77

    def test_get_name_correct_name(self):
        new_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Тестовый', 77)
        assert new_ingredient.get_name() == 'Соус Тестовый'

    @pytest.mark.parametrize('type, exp_type', ([INGREDIENT_TYPE_SAUCE, 'SAUCE'], [INGREDIENT_TYPE_FILLING, 'FILLING']))
    def test_get_type_correct_type(self, type, exp_type):
        ingredient = Ingredient(type, 'Тестовая начинка', 77)
        assert ingredient.get_type() == exp_type
