import ProductFile

class CartItem:
    _title = ""
    _quantity = 0
    _price = 0
    _total = 0

    def __init__(self, product:ProductFile.Product):
        self._title = product._title
        self._quantity = 1
        self._price = product._price
        self._total = self._quantity * self._price