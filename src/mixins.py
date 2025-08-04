class InitMessageMixin:
    def __init__(self, name, description, price, quantity):
        print(
            f"Создан объект класса {self.__class__.__name__} с параметрами: "
            f"{name}, {description}, {price}, {quantity}"
        )
        super().__init__(name, description, price, quantity)
