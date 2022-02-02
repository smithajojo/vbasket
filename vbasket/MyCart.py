import Product
import ShoppingCart
import ProductManager

sc = ShoppingCart.ShoppingCart()

# sc.AddItem(Product.Product("LAP","Laptop",300))
# sc.AddItem(Product.Product("SPR","Speaker",100))
# sc.AddItem(Product.Product("LAP","Laptop",300))
# sc.AddItem(Product.Product("COM","Computer",270))
# sc.AddItem(Product.Product("MON","Monitor",150))
# sc.AddItem(Product.Product("LAP","Laptop",300))
# sc.AddItem(Product.Product("COM","Computer",270))
# sc.AddItem(Product.Product("LAP","Laptop",300))
# sc.AddItem(Product.Product("LAP","Laptop",300))
#
# sc.DisplayCart()

pm = ProductManager.PManager()
sc.AddItem(pm.GetRandomProducts())
sc.AddItem(pm.GetRandomProducts())
sc.DisplayCart()
