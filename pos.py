class PointOfSale():
    def __init__(self, display):
        self.display = display

    def on_barcode(self, barcode):
        if barcode == "12345":
            self.display.display_text("$9.50")
        elif barcode == "98765":
            self.display.display_text("$1.50")
        else:
            self.display.display_text("Item with barcode 99999 not found")


class Display:
    def get_text(self):
        return self.__text

    def display_text(self, value):
        self.__text = value

