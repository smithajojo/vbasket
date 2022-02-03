import CartItemFile
import ProductFile
class ShoppingCart:
    _cartItems:CartItemFile.CartItem = []

    def AddItem(self, prod:ProductFile.Product):
        c = CartItemFile.CartItem(prod)
        if len(self._cartItems) == 0:
            self._cartItems.append(c)
        elif not any (prod._title == ai._title for ai in self._cartItems):
             self._cartItems.append(c)
        else:
            for ci in self._cartItems:
                if prod._title == ci._title:
                    ci._quantity = ci._quantity + 1
                    ci._total = ci._quantity * ci._price

    def DeleteItem(self,prod:ProductFile.Product):
        if any(prod._title == ai._title for ai in self._cartItems):
            searchitem:CartItemFile.CartItem="";
            for ci in self._cartItems:
                if prod._title == ci._title and ci._quantity >= 1:
                    searchitem = ci
                    break;
            # if searchitem is not None and not searchitem == "":
            if searchitem._quantity == 1 :
                x = self._cartItems.index(searchitem)
                self._cartItems.pop(x)
            else :
                searchitem._quantity = searchitem._quantity - 1
                searchitem._total = searchitem._quantity * searchitem._price

    def DisplayCart(self):
        print ('\033[92m' + "Your Shopping Cart")
        print ('\033[94m'  + "************************************")
        for ci in self._cartItems:
            print(ci._title +" X " +str(ci._quantity) +" = " + str(ci._total))
        if len(self._cartItems) == 0:
            print ('\033[93m' +"Your Cart is empty")
        print('\033[94m' + "************************************")

    def CheckOut(self):
        print("Your Total Payment is 0")
        pass


