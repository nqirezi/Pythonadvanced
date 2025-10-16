class Dog:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} says hello")

class Cat:
    def __init__(self,name):
        self.name = name
    def sound(self):
        print(f"{self.name} says hi")

class Bird:
    def __init__(self,name,):
        self.name = name

    def sound(self):
        print(f"{self.name} says pershendetje")

dog = Dog
cat = Cat
bird = Bird


for animal in (dog,cat,bird):
    animal.sound()