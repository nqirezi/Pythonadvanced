#abstractions
from abc import ABC, abstractmethod


#class ClassName(ABC):
    #pass

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, length):
        self.length = length


    def area(self):
        return self.length * self.length

circle1 = Circle(2)
square1 = Square(10)
print(circle1.area())
print(square1.area())