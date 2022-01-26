from datetime import datetime
class Product:
    _name = ""
    _price = 0.00

    def __init__(self, name, price):
        self._name = name
        self._price = price

    def Show(self):
        print(self._name, "--", self._price)

class ProductList:
    _lst = []

    def AddProduct(self, product):
        self._lst.append(product)

    def RemoveProduct(self, product):
        pass

    def GetAllProducts(self):
        pass

    def ShowAllProducts(self):
        for p in self._lst:
            p.Show()

class CartItem:
    _quantity = 0
    _totPrice = 0.00
    _product = ""

    def __init__(self, product):
        self._quantity = self._quantity + 1
        self._product = product
        self._totPrice = self._quantity * self._product._price

    def UpdateQuantity(self, quantity, product):
        self._quantity = self._quantity + quantity
        self._totPrice = self._quantity * product._price

class Cart:
    _cartlst = []

    def AddToCart(self, product):
        if not any(itm._product._name == product._name for itm in self._cartlst):
            self._cartlst.append(CartItem(product))
        elif len(self._cartlst) > 0 :
            for item in self._cartlst:
                if item._product._name == product._name :
                    item._quantity = item._quantity + 1
                    item._totPrice = item._quantity * product._price

    def RemoveFromCart(self):
        pass

    def ApplyDiscounts(self):
        pass

    def CheckOut(self):
        pass

    def DisplayCart(self):
        print('\033[93m' + "Your Shopping Cart -", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print('\033[94m' + "*******************************************")
        ordertotal = 0

        for item in self._cartlst:
            print(item._product._name,' > ',item._product._price,' X ',item._quantity,' = ',item._totPrice)
            ordertotal = ordertotal+item._totPrice
        print("*******************************************")
        print('\033[92m' + "Grand Total Price = ",ordertotal)

c = Cart()
c.AddToCart(Product("Laptop", 75))
c.AddToCart(Product("Mobile",50))
c.AddToCart(Product("Mobile",50))
c.AddToCart(Product("Mobile",50))
c.AddToCart(Product("Mobile",50))
c.AddToCart(Product("Laptop", 75))
c.DisplayCart()
