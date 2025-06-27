import json
from typing import List

from src.models import Category, Product


def load_data_from_json(filepath: str) -> List[Category]:
    """Загружает категории и товары из JSON-файла, возвращает список Category."""

    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)

    categories: List[Category] = []
    for cat in data:
        prods = [
            Product(
                name=prod["name"],
                description=prod["description"],
                price=float(prod["price"]),
                quantity=int(prod["quantity"])
            )
            for prod in cat.get("products", [])
        ]
        category = Category(
            name=cat["name"],
            description=cat["description"],
            products=prods
        )
        categories.append(category)

    return categories
