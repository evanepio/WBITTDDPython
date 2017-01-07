class PointOfSale():
    def __init__(self, display, catalog):
        self.display = display
        self.catalog = catalog

    def on_barcode(self, barcode):
        if not barcode:
            self.display_invalid_barcode_message()
            return

        if barcode in self.catalog.keys():
            self.display_message(self.catalog[barcode])
        else:
            self.display_item_not_found_message(barcode)

    def display_item_not_found_message(self, barcode):
        self.display_message("Item with barcode {} not found".format(barcode))

    def display_invalid_barcode_message(self):
        self.display_message("The barcode is invalid")

    def display_message(self, message):
        self.display.display_text(message)


class Display:
    def __init__(self):
        self.text = ""

    def get_text(self):
        return self.text

    def display_text(self, value):
        self.text = value

