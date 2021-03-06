from pos import Display, PointOfSale, Catalog


def test_item_found():
    display = Display()
    sut = PointOfSale(display, Catalog({"12345": 9.50, "98765": 1.50}))

    sut.on_barcode("12345")

    assert display.get_text() == "$9.50"


def test_another_item_found():
    display = Display()
    sut = PointOfSale(display, Catalog({"12345": 9.50, "98765": 1.50}))

    sut.on_barcode("98765")

    assert display.get_text() == "$1.50"


def test_item_not_found():
    display = Display()
    sut = PointOfSale(display, Catalog({"12345": 9.50}))

    sut.on_barcode("99999")

    assert display.get_text() == "Item with barcode 99999 not found"


def test_another_item_not_found():
    display = Display()
    sut = PointOfSale(display, Catalog({"12345": 9.50}))

    sut.on_barcode("76543")

    assert display.get_text() == "Item with barcode 76543 not found"


def test_empty_barcode():
    display = Display()
    sut = PointOfSale(display, Catalog({}))

    sut.on_barcode('')

    assert display.get_text() == "The barcode is invalid"
