class PointOfSale():
    def on_barcode(selfself, barcode):
        pass

class Display:
    def get_text(self):
        return "$9.50"

def test_item_found():
    sut = PointOfSale()
    display = Display()

    # Test
    sut.on_barcode('12345')

    assert display.get_text() == "$9.50"