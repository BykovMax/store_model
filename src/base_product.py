from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__()  # Важно для работы миксина!
        self._name = name
        self._description = description
        self._price = price
        self._quantity = quantity

    @property
    def price(self):
        return self._price

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self._price:
            confirm = input(f"Вы действительно хотите понизить цену с {self._price} до {new_price}? (y/n): ")
            if confirm.lower() != "y":
                print("Изменение отменено")
                return

        self._price = new_price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        if value < 0:
            raise ValueError("Количество не может быть отрицательным")
        self._quantity = value

    def add_product(self, other: "BaseProduct"):
        if self._name == other._name and self._price == other._price:
            self._quantity += other._quantity
        else:
            raise ValueError("Нельзя объединить разные товары")

    @abstractmethod
    def __str__(self) -> str:
        pass
