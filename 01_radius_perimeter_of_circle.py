#!/bin/python
import math

class Circle(object):

    def __init__(self, radius):
        if isinstance(radius, float):
            self.radius = radius
        else:
            raise TypeError("radius must be float type")

    def perimeter(self):
        return 2 * math.pi * self.radius
    def area(self):
        return math.pi * self.radius * self.radius

if __name__ == '__main__':
    radius=5.5

    print("creating circle object with %f radius" % radius)
    Circle_obj  = Circle(radius)
    print("The perimeter of this cycle is : %.6f" % Circle_obj.perimeter())
    print("The area of this cycle is : %.6f" % Circle_obj.area())
