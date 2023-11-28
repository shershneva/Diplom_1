## Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `bun_test.py`, `burger_test.py` и т.д.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`

## Тесты: ##

Класс `TestBun`:
* `test_get_name` — тест на получение корректного имени булочки
* `test_get_price` — тест на получение корректной цены булочки

Класс `TestIngredient`:
* `test_get_name` — тест на получение корректного имени ингридиента
* `test_get_price` —  тест на получение корректной цены ингридиента
* `test_get_type` — параметризированный тест на получение корректного типа начинки

Класс `TestBurger`:
* `test_add_ingredient_added_successfully` — тест на успешное добавление ингридиента
* `test_remove_ingredient_removed_successfully` — тест на успешное удаление ингридиента
* `test_move_ingredient_moved_succesfully` — тест на успешное перемещение ингридиента
* `test_get_price_correct_price` — тест на получение корректной цены ингридиентов
* `test_get_receipt_correct_receipt` — тест на получение корректного рецепта бургера
