class Product:
    def __init__(self, code,name, price):
        self.cd=code
        self.nm=name
        self.prc=price

    def print(self):
        print(self.cd,self.nm,self.prc)

class CartItem:
    productname =""
    quantitypurchased =0
    producttotalprice =0
    def __init__(self,productx,quantityadded):
        self.productname =productx.nm
        self.quantitypurchased = quantityadded
        self.producttotalprice = productx.prc * self.quantitypurchased

    def print(self):
        print(self.productname,self.quantitypurchased,self.producttotalprice)

item = Product("A001","Apple",2.5)
item.print()
citem = CartItem(item,4)
citem.print()

