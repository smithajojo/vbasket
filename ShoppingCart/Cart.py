class Product:
    _name = ""
    _price = 0.00

    def __init__(self,name,price):
        self._name = name
        self._price = price
    def Show(self):
        print(self._name,"--",self._price)

class ProductList:
    _lst = []
    def AddProduct(self,product):
        self._lst.append(product)

    def RemoveProduct(self,product):
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

    def __init__(self,product):
        self._quantity = self._quantity + 1
        self._product = product
        self._totPrice = self._quantity * self._product._price

    def UpdateQuantity(self,quantity,product):
        self._quantity = self._quantity + quantity
        self._totPrice = self._quantity * product._price

class Cart:
    _cartlst = []
    def AddToCart(self,product):

        self._cartlst.append(CartItem(product))
        pass
    def RemoveFromCart(self):
        pass

    def ApplyDiscounts(self):
        pass
    def CheckOut(self):
        pass

    def DisplayCart(self):
        for item in self._cartlst:
            print(item._product._name)


c = Cart()
c.AddToCart(Product("Laptop",300))
c.DisplayCart()