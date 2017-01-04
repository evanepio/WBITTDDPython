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


def test_item_not_found():
    display = Display()
    sut = PointOfSale(display)

    sut.on_barcode("99999")

    assert display.get_text() == "Item with barcode 99999 not found"


def test_another_item_not_found():
    display = Display()
    sut = PointOfSale(display)

    sut.on_barcode("76543")

    assert display.get_text() == "Item with barcode 76543 not found"