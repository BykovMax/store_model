from src.product import Product


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: str, model: str, memory: str, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


# if __name__ == "__main__":
#     product = Smartphone("Honor 200 Pro", "смартфон", 50999, 3,
#                          "Процессор Qualcomm Snapdragon 8s Gen 3 совместно с 12 ГБ оперативной",
#                          "HONOR 200 Pro", "512 ГБ",
#                          "Черный")
#     print(product.name)
#     print(product.description)
#     print(product.price)
#     print(product.quantity)
#     print(product.efficiency)
#     print(product.model)
#     print(product.memory)
#     print(product.color)
