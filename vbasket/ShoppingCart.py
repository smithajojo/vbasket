import Product
import ProductCart


class ShoppingCart:
    cartItems: ProductCart.CartItem = []

    def AddItem(self, product: Product.Product):
        cartItem = ProductCart.CartItem(product)
        if len(self.cartItems) == 0:
            self.cartItems.append(cartItem)
        elif not any(product.pcode == item.pcode for item in self.cartItems):
            self.cartItems.append(cartItem)
        else:
            for p in self.cartItems:
                if product.pname == p.pname:
                    p.pquantity = p.pquantity + 1
                    p.ptotal = p.pquantity * p.pprice

    def DisplayCart(self):

        for ci in self.cartItems:
            print(ci.pcode,ci.pname,str(ci.pprice) +" X " +str(ci.pquantity) +" = " + str(ci.ptotal))
        if len(self.cartItems) == 0:
            print ("Your Cart is empty")
        print("************************************")