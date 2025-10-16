#Key OOP principles (Encapsulation,Inheritance,Polymorphism,Abstraction)

#Inheritance

#class SuperClass:
  #
  # class Subclass(SuperClass):

class Animal:
    def  sound(self):
        print("Some generic animal sound")


#class Dog(Animal):
 #   def bark(self):
  #      print("it barks")
    #def eat(self):
     #   print("it eats"):


class Cat(Animal):
    def sound(self):
        print("Cat sound")
class Dog(Animal):
    def Dog(self):
        print("Dog sound")


animal = Animal()
animal.sound()

cat = Cat()
cat.sound()
dog = Dog()
dog.sound()