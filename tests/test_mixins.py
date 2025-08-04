from src.product import Product


def test_init_message_mixin_output(capsys):
    product = Product(
        name="LG OLED TV",
        description="55 дюймов, 4K HDR, Smart TV",
        price=120000,
        quantity=2
    )

    captured = capsys.readouterr()
    assert (
            "Создан объект класса Product с параметрами: LG OLED TV, 55 дюймов, 4K HDR, Smart TV, 120000, 2"
            in captured.out
    )
