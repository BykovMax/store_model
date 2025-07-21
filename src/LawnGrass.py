from src.product import Product


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


# if __name__ == "__main__":
#     grass = LawnGrass("Газонная трава", "Универсальная смесь", 1500.0, 50, "Россия", "7 дней", "Зеленый")
#
#     print(grass.name)
#     print(grass.description)
#     print(grass.price)
#     print(grass.quantity)
#     print(grass.country)
#     print(grass.germination_period)
#     print(grass.color)
