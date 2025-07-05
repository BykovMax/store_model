class Product:
    """Класс для представления товара в магазине."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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

    @property
    def price(self):
        """Возвращает текущую цену товара."""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Устанавливает новую цену товара."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            confirm = input(f"Вы действительно хотите понизить цену с {self.__price} до {new_price}? (y/n): ")
            if confirm.lower() != "y":
                print("Изменение отменено")
                return

        self.__price = new_price
