import json

import pytest

from src.category import Category
from src.loaders import load_data_from_json

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

    product_lines = cat.products.strip().split("\n")
    assert len(product_lines) == 2
    assert "Книга А" in product_lines[0]
    assert "Книга Б" in product_lines[1]


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

        product_lines = [line for line in cat.products.strip().split("\n") if line]
        assert len(product_lines) == expected["prod_count"]

        if expected["prod_count"]:
            assert expected["prod_name"] in product_lines[0]
