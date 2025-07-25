from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self._name = name
        self._description = description
        self._price = price
        self._quantity = quantity

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = value

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        if value < 0:
            raise ValueError("Количество не может быть отрицательным")
        self._quantity = value

    def add_product(self, other: "BaseProduct") -> None:
        """Увеличивает количество товара, если названия и цена совпадают"""
        if (
                self._name == other._name
                and self._price == other._price
        ):
            self._quantity += other._quantity
        else:
            raise ValueError("Нельзя объединить разные товары")

    @abstractmethod
    def __str__(self) -> str:
        pass
