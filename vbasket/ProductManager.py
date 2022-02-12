import os.path

import Product
import  random
class PManager:
    plist:Product.Product = []

    def AddItem(self,product:Product.Product):
        if len(self.plist) == 0:
            self.plist.append(product)
        elif not any (product.pcode == item.pcode for item in self.plist):
             self.plist.append(product)


    def GetAllProducts(self):
        return self.plist

    def GetRandomProducts(self):
        self.BuildProducts()
        if(len(self.plist)>0):
            rn = random.randint(1,len(self.plist))
            return self.plist[rn-1]

    def BuildProducts(self):
        p1 = Product.Product("LAP","Laptop",500)
        self.AddItem(p1)
        p2 = Product.Product("COM","Computer",270)
        self.AddItem(p2)
        p3 = Product.Product("MON","Monitor",150)
        self.AddItem(p3)

    def ReadProducts(self):
        filepath = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
        print(filepath)
        actualfile = os.path.join(filepath, 'vbasket\\Data\\Product.json')
