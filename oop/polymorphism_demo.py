import math

# Base Class - Shape
class Shape:
    def area(self):
        """This method should be overridden in derived classes."""
        raise NotImplementedError("The area method must be overridden in subclasses")


# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initializes the Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Overrides the area method to calculate the area of a rectangle."""
        return self.length * self.width


# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initializes the Circle with a radius."""
        self.radius = radius

    def area(self):
        """Overrides the area method to calculate the area of a circle."""
        return math.pi * (self.radius ** 2)
