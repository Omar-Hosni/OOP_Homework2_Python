import math
import cmath
#Problem 2 Homework OOP

#Volume and Surface area of a cylinder using height and radius

class Cylinder:
    def __init__(self,height = 1, radius =1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * (self.radius**2) * self.height

    def surface_area(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius**2))


c1 = Cylinder(2,3)
print(float(c1.volume()))
print(float(c1.surface_area()))
