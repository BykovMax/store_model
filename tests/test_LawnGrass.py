# =============================
# ====== тесты LawnGrass ======
# =============================

def test_lawngrass_init(sample_lawngrass):
    assert sample_lawngrass.name == "Универсальная трава"
    assert sample_lawngrass.description == "Смесь для газонов"
    assert sample_lawngrass.price == 1500
    assert sample_lawngrass.quantity == 20
    assert sample_lawngrass.country == "Россия"
    assert sample_lawngrass.germination_period == "7 дней"
    assert sample_lawngrass.color == "Зеленый"
