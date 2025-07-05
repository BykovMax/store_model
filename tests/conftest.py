import json

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_product():
    return Product(
        name="Honor 200 Pro",
        description="512 ГБ, черный, 12 ГБ, 2 SIM, камера 50+50+12 МП",
        price=50999,
        quantity=2
    )


@pytest.fixture
def sample_products():
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    ]


@pytest.fixture
def category(sample_products):
    return Category(
        name="Смартфоны",
        description=(
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций для удобства жизни"
        ),
        products=sample_products
    )


@pytest.fixture
def tmp_json_file(tmp_path):
    """Создает временный JSON-файл с одной категорией и двумя продуктами."""
    data = [
        {
            "name": "Книги",
            "description": "Разные книги",
            "products": [
                {"name": "Книга А", "description": "Описание A", "price": "100.5", "quantity": "3"},
                {"name": "Книга Б", "description": "Описание B", "price": 200, "quantity": 2}
            ]
        }
    ]
    file_path = tmp_path / "test_data.json"
    file_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return str(file_path)
