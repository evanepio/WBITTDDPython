class PointOfSale():
    def __init__(self, display):
        self.display = display
        self.catalog = {"12345": "$9.50", "98765": "$1.50"}

    def on_barcode(self, barcode):
        if not barcode:
            self.display.display_text("The barcode is invalid")
            return

        if barcode in self.catalog.keys():
            self.display.display_text(self.catalog[barcode])
        else:
            self.display.display_text("Item with barcode {} not found".format(barcode))


class Display:
    def get_text(self):
        return self.__text

    def display_text(self, value):
        self.__text = value

