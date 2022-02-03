import ProductFile
import ShoppingCartFile

sc = ShoppingCartFile.ShoppingCart()
sc.AddItem(ProductFile.Product("Apple", 0.50))
sc.AddItem(ProductFile.Product("Apple", 0.50))
sc.AddItem(ProductFile.Product("Apple", 0.50))
sc.AddItem(ProductFile.Product("Orange", 0.20))
sc.AddItem(ProductFile.Product("Orange", 0.20))
sc.AddItem(ProductFile.Product("Banana", 0.20))

sc.DisplayCart()
sc.DeleteItem(ProductFile.Product("Apple", 0.50))
sc.DeleteItem(ProductFile.Product("Apple", 0.50))
sc.DisplayCart()
sc.DeleteItem(ProductFile.Product("Apple", 0.50))
sc.DisplayCart()
sc.CheckOut()
