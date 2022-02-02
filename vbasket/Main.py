import ProductManager
import Product

pm = ProductManager.PManager()

pm.AddItem(Product.Product("LAP","Laptop",300))
pm.AddItem(Product.Product("SPR","Speaker",100))
pm.AddItem(Product.Product("LAP","Laptop",300))
pm.AddItem(Product.Product("COM","Computer",270))
pm.GetAllProducts()

for item in pm.GetAllProducts():
    print(item.pcode, item.pname, item.pprice)

prodct:Product = pm.GetRandomProducts()
print(prodct.pname)
