# ==============================
# ====== тесты Smartphone ======
# ==============================

def test_smartphone_init(sample_smartphone):
    assert sample_smartphone.name == "Honor 200 Pro"
    assert sample_smartphone.description == "смартфон"
    assert sample_smartphone.price == 50999
    assert sample_smartphone.quantity == 3
    assert sample_smartphone.efficiency == "Qualcomm Snapdragon 8s Gen 3"
    assert sample_smartphone.model == "HONOR 200 Pro"
    assert sample_smartphone.memory == "512 ГБ"
    assert sample_smartphone.color == "Черный"
