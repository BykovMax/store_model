import json

import pytest

from src.loaders import load_data_from_json
from src.category import Category
from src.product import Product

# =================================
# ====== load_data_from_json ======
# =================================

def test_load_data_from_json(tmp_json_file):
    cats = load_data_from_json(tmp_json_file)
    assert isinstance(cats, list)
    assert len(cats) == 1

    cat = cats[0]
    assert isinstance(cat, Category)
    assert cat.name == "Книги"
    assert cat.description == "Разные книги"
    assert len(cat.products) == 2

    prod1, prod2 = cat.products
    assert isinstance(prod1, Product)
    assert prod1.name == "Книга А"
    assert prod1.price == 100.5
    assert prod1.quantity == 3
    assert isinstance(prod2.price, float)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            [
                {
                    "name": "Книги",
                    "description": "Художественные книги",
                    "products": [
                        {"name": "1984", "description": "Оруэлл", "price": "150", "quantity": "1"}
                    ]
                }
            ],
            {"cat_name": "Книги", "prod_count": 1, "prod_name": "1984"}
        ),
        (
            [],
            None
        ),
        (
            [
                {
                    "name": "Одежда",
                    "description": "Мужская одежда",
                    "products": []
                }
            ],
            {"cat_name": "Одежда", "prod_count": 0}
        ),
    ]
)
def test_load_data_from_json_parametrized(tmp_path, input_data, expected):
    file_path = tmp_path / "test_data.json"
    file_path.write_text(json.dumps(input_data, ensure_ascii=False), encoding="utf-8")

    result = load_data_from_json(str(file_path))

    if expected is None:
        assert result == []
    else:
        assert isinstance(result, list)
        assert len(result) == 1

        cat = result[0]
        assert isinstance(cat, Category)
        assert cat.name == expected["cat_name"]
        assert isinstance(cat.products, list)
        assert len(cat.products) == expected["prod_count"]

        if cat.products:
            product = cat.products[0]
            assert isinstance(product, Product)
            assert product.name == expected["prod_name"]
