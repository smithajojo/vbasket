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

x = Product(101,'MT101J','Speaker',20)
y = Product(101,'MT101Q','Mouse',28)

lst = []
lst.append(x)
lst.append(y)
print(len(lst))

for pro in lst:
    pro.info()



# Task One
# Declare an array
# Add 3 product to array
# Iterate the array and print the products

# Create a class called CartItem which accepts product , index and qty,
#add price, actual price, total price
#
# Create a shopping Cart class
# Create a method to add Product to cart
# Crete an array to store CartItems
# Create a methods to remove item from cart
# Create a method to calculate the total Price of the cart