import pytest

from src.category import Category
from src.product import Product


# ===========================
# ====== тесты Category =====
# ===========================

def test_category_init(category):
    assert category.name == "Смартфоны"
    assert category.description == (
        "Смартфоны, как средство не только коммуникации,"
        " но и получения дополнительных функций для удобства жизни"
    )
    expected = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )
    assert category.products == expected


def test_category_str(category):
    assert str(category) == "Смартфоны, количество продуктов: 27 шт."


def test_category_class_counters(sample_products):
    # Сбросим счётчики, чтобы не зависеть от других тестов
    Category.category_count = 0
    Category.product_count = 0

    # Создаём первую категорию с тремя товарами
    Category("Смартфоны", "Описание 1", sample_products)

    # Проверяем, что счётчики обновились корректно
    assert Category.category_count == 1
    assert Category.product_count == 3

    # Создаём вторую категорию, но только с ОДНИМ товаром из списка
    Category("Телевизоры", "Описание 2", sample_products[:1])

    # Проверяем, что счётчики увеличились: категорий стало 2, а товаров 4
    assert Category.category_count == 2
    assert Category.product_count == 4


def test_category_add_product(category):
    product = Product("iPhone 15", "512 GB", 100000, 1)
    initial_count = len(category._Category__products)
    category.add_product(product)
    assert len(category._Category__products) == initial_count + 1
    assert product in category._Category__products


def test_category_products_property(category):
    result = category.products
    assert isinstance(result, str)
    for product in category._Category__products:
        assert product.name in result
        assert str(product.price) in result
        assert str(product.quantity) in result


def test_add_invalid_product_type(category):
    with pytest.raises(TypeError):
        category.add_product("не продукт")


def test_average_price_with_products():
    products = [
        Product("Samsung", "Смартфон", 100_000, 5),
        Product("iPhone", "Смартфон", 120_000, 3),
        Product("Xiaomi", "Смартфон", 60_000, 10),
    ]
    category = Category("Смартфоны", "Мобильные устройства", products)
    expected_average = (100_000 + 120_000 + 60_000) / 3
    assert category.average_price() == expected_average


def test_average_price_empty_category():
    empty_category = Category("Пустая", "Нет товаров", [])
    assert empty_category.average_price() == 0
