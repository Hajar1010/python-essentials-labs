import math

class Rectangle:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        
    def area(self):
        return self.side1 * self.side2

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * (self.radius ** 2)