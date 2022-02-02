import Product

class CartItem:
    pcode = ""
    pname = ""
    pquantity = 0
    pprice = 0
    ptotal = 0

    def __init__(self,product:Product.Product):
        self.pcode = product.pcode
        self.pname = product.pname
        self.pquantity = 1
        self.pprice = product.pprice
        self.ptotal = self.pprice
