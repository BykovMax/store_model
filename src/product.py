from src.base_product import BaseProduct
from src.mixins import InitMessageMixin


class Product(InitMessageMixin, BaseProduct):
    """Класс для представления товара в магазине."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов.")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, data: dict, existing_products: list["Product"] = None) -> "Product":
        """Создаёт новый объект Product из словаря данных."""
        existing_products = existing_products or []

        # Поиск товара с тем же именем
        for prod in existing_products:
            if prod.name == data["name"]:
                # Обновляем количество
                prod.quantity += int(data["quantity"])
                # Обновляем цену, если новая выше
                new_price = float(data["price"])
                if new_price > prod.price:
                    prod.price = new_price
                return prod

        # Если не нашли, создаём новый
        return cls(
            name=data["name"],
            description=data["description"],
            price=float(data["price"]),
            quantity=int(data["quantity"])
        )


# if __name__ == "__main__":
#     product = Product("MacBook", "Ноутбук от Apple", 120000, 3)
#     print(product)  # Ожидается: MacBook, 120000 руб. Остаток: 3 шт.
