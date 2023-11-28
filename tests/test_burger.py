import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Тестовая булочка'
        mock_bun.get_price.return_value = 77.7
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun


    def test_add_ingredient_added_successfully(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.type = 'SAUCE'
        mock_ingredient.name = 'Тестовая начинка'
        mock_ingredient.price = 100.1
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient]


    def test_remove_ingredient_removed_successfully(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        burger.ingredients = [mock_ingredient2, mock_ingredient1]
        burger.remove_ingredient(0)

        assert mock_ingredient2 not in burger.ingredients

    def test_move_ingredient_moved_succesfully(self):
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        burger.ingredients = [mock_ingredient2, mock_ingredient1]
        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_ingredient1, mock_ingredient2]

    def test_get_price_correct_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 77.7
        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 100.1
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 99.9

        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient1, mock_ingredient2]

        assert burger.get_price() == 355.4

    def test_get_receipt_correct_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Тестовая булочка'
        mock_ingredient1 = Mock()
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient1.get_name.return_value = 'Тестовая начинка'
        mock_ingredient2 = Mock()
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient2.get_name.return_value = 'Тестовый соус'
        mock_burger = Mock()
        mock_burger.get_price.return_value = 355.4

        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        burger.get_price = mock_burger.get_price

        expected_receipt = '(==== Тестовая булочка ====)\n' \
                           '= filling Тестовая начинка =\n' \
                           '= sauce Тестовый соус =\n' \
                           '(==== Тестовая булочка ====)\n' \
                           '\nPrice: 355.4'

        assert burger.get_receipt() == expected_receipt
