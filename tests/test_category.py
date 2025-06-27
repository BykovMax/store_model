from src.category import Category


# ===========================
# ====== тесты Category =====
# ===========================

def test_category_init(category, sample_products):
    assert category.name == "Смартфоны"
    assert (category.description ==
            "Смартфоны, как средство не только коммуникации,"
            " но и получения дополнительных функций для удобства жизни")
    assert category.products == sample_products


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
