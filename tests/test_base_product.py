import pytest

from src.product import Product


@pytest.mark.parametrize(
    "initial_price,new_price,user_input,expected_price,expected_output",
    [
        (50999, 60000, None, 60000, ""),  # Повышение — проходит
        (50999, 45000, "y", 45000, ""),  # Понижение с подтверждением
        (50999, 40000, "n", 50999, "Изменение отменено"),  # Понижение с отказом
        (50999, -1000, None, 50999, "Цена не должна быть нулевая или отрицательная"),  # Отрицательная
    ]
)
def test_price_setter_behavior(monkeypatch, capsys, initial_price, new_price, user_input, expected_price,
                               expected_output):
    product = Product(
        name="Honor 200 Pro",
        description="512 ГБ, черный",
        price=initial_price,
        quantity=1
    )

    if user_input is not None:
        monkeypatch.setattr("builtins.input", lambda _: user_input)

    product.price = new_price
    captured = capsys.readouterr()

    assert product.price == expected_price
    if expected_output:
        assert expected_output in captured.out


def test_quantity_setter_valid(sample_product):
    sample_product.quantity = 10
    assert sample_product.quantity == 10


def test_quantity_setter_negative_raises(sample_product):
    with pytest.raises(ValueError):
        sample_product.quantity = -1


def test_add_product_successful():
    samsung1 = Product("Samsung Galaxy A72", "128GB, Синий", 35000.0, 2)
    samsung2 = Product("Samsung Galaxy A72", "128GB, Синий", 35000.0, 3)

    samsung1.add_product(samsung2)
    assert samsung1.quantity == 5


def test_add_product_incompatible_raises():
    samsung = Product("Samsung Galaxy A72", "128GB, Синий", 35000.0, 2)
    iphone = Product("iPhone 14", "128GB, Черный", 110000.0, 3)

    with pytest.raises(ValueError):
        samsung.add_product(iphone)
