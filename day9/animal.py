class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Some generic animal sound")
    def desc(self):
        print(f"this animal is named {self.name}")

class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("Dog sound")

    def desc(self):
        super().desc()
        print(f"Breed {self.breed}")


class Cat(Animal):
    def __init__(self, name,color):
        super().__init__(name)
        self.color = color
    def sound(self):
        print("Cat sound")
    def desc(self):
        super().desc()
        print(f"Cat {self.color} sound")

animal = Animal("Generic Animal")
animal.sound()
animal.desc()

dog = Dog("Max","Golden Retriver")
dog.sound()
dog.desc()

cat = Cat("Green","Blue")
cat.sound()
cat.desc()