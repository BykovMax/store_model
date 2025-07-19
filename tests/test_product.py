from src.product import Product


# ===========================
# ====== тесты Product ======
# ===========================

def test_product_init(sample_product):
    assert sample_product.name == "Honor 200 Pro"
    assert sample_product.description == "512 ГБ, черный, 12 ГБ, 2 SIM, камера 50+50+12 МП"
    assert sample_product.price == 50999
    assert sample_product.quantity == 2


def test_product_str(sample_product):
    assert str(sample_product) == "Honor 200 Pro, 50999 руб. Остаток: 2 шт."


def test_product_addition():
    p1 = Product("Товар 1", "Описание 1", 100, 3)  # 100 * 3 = 300
    p2 = Product("Товар 2", "Описание 2", 200, 2)  # 200 * 2 = 400
    total = p1 + p2
    assert total == 700


def test_product_price_getter_setter(sample_product):
    assert sample_product.price == 50999
    sample_product.price = 130000
    assert sample_product.price == 130000

    sample_product.price = -100  # цена не должна измениться
    assert sample_product.price == 130000


def test_product_price_setter_with_lower_price(monkeypatch, sample_product):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    sample_product.price = 100000
    assert sample_product.price == 100000

    monkeypatch.setattr("builtins.input", lambda _: "n")
    sample_product.price = 90000
    assert sample_product.price == 100000


def test_new_product_without_duplicates():
    data = {"name": "MacBook Pro", "description": "M3, 16GB RAM", "price": 250000, "quantity": 5}
    new_prod = Product.new_product(data)
    assert isinstance(new_prod, Product)
    assert new_prod.name == "MacBook Pro"
    assert new_prod.price == 250000
    assert new_prod.quantity == 5


def test_new_product_with_duplicates():
    existing = [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000, 3),
    ]
    data = {"name": "Samsung Galaxy S23 Ultra", "description": "новый", "price": 185000, "quantity": 2}
    new_prod = Product.new_product(data, existing)

    assert new_prod.name == "Samsung Galaxy S23 Ultra"
    assert new_prod.quantity == 5
    assert new_prod.price == 185000
    assert len(existing) == 1
