class PointOfSale:
    def __init__(self, display, price_by_barcode):
        self.display = display
        self.price_by_barcode = price_by_barcode

    def on_barcode(self, barcode):
        if not barcode:
            self.display.display_invalid_barcode_message()
            return

        price = self.get_price_from_barcode(barcode)

        if price is not None:
            self.display.display_price(price)
        else:
            self.display.display_item_not_found_message(barcode)

    def get_price_from_barcode(self, barcode):
        return self.price_by_barcode.get(barcode, None)


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
        self.text = "${:.2f}".format(price)

    def display_message(self, message):
        self.text = message
