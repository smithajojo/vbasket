class Product:
    def __init__(self, id, code, name, price):
        self.id = id
        self.code = code
        self.name = name
        # self.price = price
        if (price > 10 and price < 50) :
            self.price = price
        else:
            raise ValueError('10<Price<50')

    def info(self):
        print(self.id,self.code,self.name,self.price)

class CartItem:
    price = 0.0
    act_price = 0.0
    tot_price = 0.0
    def __init__(self, product, index, quanty):
        self.prd = product
        self.ind = index
        self.qty = quanty
        self.price = product.price
        self.act_price = product.price
        self.tot_price = product.price

    def show_items(self):
        print("Hello")
        print(self.ind,self.qty,self.price,self.act_price,self.tot_price)
        print("Bye")

pro = Product(101,'MT101J','Speaker',20)
citem = CartItem(pro,'1212LP',4)
citem.show_items()
