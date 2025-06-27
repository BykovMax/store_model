from src.loaders import load_data_from_json
from src.category import Category


def main():
    categories: list[Category] = load_data_from_json("data/sample_data.json")  # путь к файлу с данными

    print("Загруженные категории и товары:\n")
    for category in categories:
        print(f"Категория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Количество товаров: {len(category.products)}")
        for product in category.products:
            print(f" - {product.name} | {product.price} руб. | {product.quantity} шт.")
        print()

    print("Статистика:")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")


if __name__ == "__main__":
    main()
