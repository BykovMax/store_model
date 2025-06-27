# ===========================
# ====== тесты Product ======
# ===========================

def test_product_init(sample_product):
    assert sample_product.name == "Honor 200 Pro"
    assert sample_product.description == "512 ГБ, черный, 12 ГБ, 2 SIM, камера 50+50+12 МП"
    assert sample_product.price == 50999
    assert sample_product.quantity == 2
