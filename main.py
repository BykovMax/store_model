from src.category import Category
from src.loaders import load_data_from_json


def main():
    categories: list[Category] = load_data_from_json("data/sample_data.json")

    print("Загруженные категории и товары:\n")
    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Количество товаров: {len(category.products_list)}")  # или len(...) если хочешь по категориям
        print(category.products)  # ← используем геттер как строку
        print()

    print("Статистика:")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")


if __name__ == "__main__":
    main()
