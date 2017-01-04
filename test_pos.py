from pos import Display, PointOfSale


def test_item_found():
    display = Display()
    sut = PointOfSale(display)

    sut.on_barcode("12345")

    assert display.get_text() == "$9.50"


def test_another_item_found():
    display = Display()
    sut = PointOfSale(display)

    sut.on_barcode("98765")

    assert display.get_text() == "$1.50"