class PointOfSale():
    def __init__(self, display):
        self.display = display

    def on_barcode(self, barcode):
        if not barcode:
            self.display.display_text("The barcode is invalid")
            return

        catalog = {"12345": "$9.50", "98765": "$1.50"}

        if barcode == "12345":
            self.display.display_text(catalog["12345"])
        elif barcode == "98765":
            self.display.display_text("$1.50")
        else:
            self.display.display_text("Item with barcode {} not found".format(barcode))


class Display:
    def get_text(self):
        return self.__text

    def display_text(self, value):
        self.__text = value

