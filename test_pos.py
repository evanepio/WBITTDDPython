class PointOfSale():
    def __init__(self, display):
        self.display = display

    def on_barcode(self, barcode):
        if barcode == "12345":
            self.display.display_text("$9.50")
        elif barcode == "98765":
            self.display.display_text("$1.50")


class Display:
    def get_text(self):
        return self.__text

    def display_text(self, value):
        self.__text = value


def test_item_found():
    display = Display()
    sut = PointOfSale(display)

    # Test
    sut.on_barcode("12345")

    assert display.get_text() == "$9.50"


def test_another_item_found():
    display = Display()
    sut = PointOfSale(display)

    sut.on_barcode("98765")

    assert display.get_text() == "$1.50"