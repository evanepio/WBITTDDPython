class PointOfSale():
    def __init__(self, display, catalog):
        self.display = display
        self.catalog = catalog

    def on_barcode(self, barcode):
        if not barcode:
            self.display.display_text("The barcode is invalid")
            return

        if barcode in self.catalog.keys():
            self.display.display_text(self.catalog[barcode])
        else:
            self.display.display_text("Item with barcode {} not found".format(barcode))


class Display:
    def __init__(self):
        self.text = ""

    def get_text(self):
        return self.text

    def display_text(self, value):
        self.text = value

