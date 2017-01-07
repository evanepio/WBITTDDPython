class PointOfSale:
    def __init__(self, display, catalog):
        self.display = display
        self.catalog = catalog

    def on_barcode(self, barcode):
        if not barcode:
            self.display.display_invalid_barcode_message()
            return

        if barcode in self.catalog.keys():
            self.display.display_price(self.catalog[barcode])
        else:
            self.display.display_item_not_found_message(barcode)


class Display:
    def __init__(self):
        self.text = ""

    def get_text(self):
        return self.text

    def display_item_not_found_message(self, barcode):
        self.text = "Item with barcode {} not found".format(barcode)

    def display_invalid_barcode_message(self):
        self.text = "The barcode is invalid"

    def display_price(self, price):
        self.text = "${:.2f}".format(float(price))

    def display_message(self, message):
        self.text = message
