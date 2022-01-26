class Cuboid:
    name = "Cuboid"

    def __init__(self, length, breadth, height, weight):
        self.length = length
        self.breadth = breadth
        self.height = height
        self.weight = weight

    def volume(self,y):
        print("The y is:", y)
        x = self.length + y
        print("The x is:", x)
        y = self.breadth
        z = self.height
        v = x * y * z
        print("The volume is:", v)

    def density(self):
        x = self.length
        y = self.breadth
        z = self.height
        v = x * y * z
        d = self.weight / v
        print("Density is:", d)

    def surface_area(self):
        x = self.length
        y = self.breadth
        z = self.height
        s = 2 * (x * y + y * z + x * z)
        print("The surface area is:", s)

x = Cuboid(10,5,2,4)
x.volume(4)
x.density()
x.surface_area()


class CuboidN:
    name = "Cuboid"

    def volume(self, length, breadth, height, weight):
        x = length
        y = breadth
        z = height
        v = x * y * z
        print("The volume is:", v)

    def density(self, length, breadth, height, weight):
        x = length
        y = breadth
        z = height
        v = x * y * z
        d = weight / v
        print("Density is:", d)

    def surface_area(self, length, breadth, height, weight):
        x = length
        y = breadth
        z = height
        s = 2 * (x * y + y * z + x * z)
        print("The surface area is:", s)


print("**********************")

x = CuboidN()
x.volume(10,5,2,4)
x.density(15,5,2,4)
x.surface_area(10,15,2,4)

import random
print("Random Value "+ str(random.randrange(1,5)))