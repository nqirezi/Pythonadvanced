#def calculate_area(length,width):
 #   return length * width
from Python.module4 import greet


#def calculate_perimeter(length,width):
 #   return 2 * (length + width)

#length = 5
#width = 3

#area = calculate_area(length,width)
#perimeter = calculate_perimeter(length,width)

#print(f"Area of area is {area}")
#print(f"Perimeter of area is {perimeter}")

#class Rectangle :
    #def __init__(self, width, height):
      #  self.length = length
      #  self.width = width

     # def calculate_area(self):
      #    return self.length * self.width
      #def calculate_perimeter(self):
       #   return   self.length + self.width

     # my rectangle = Rectangle(10, 10)
    #area =  my_rectangle.calculate_area()
   #perimeter = my_rectangle.calculate_parameter

#class Person:
    #def __init__(self, name, age):
    #    self.name = name
   #     self.age = age

  #      def greet(self):
 #           print(f"Hello,{self.name},you are {self.age} years old!")


#person1 =Person ("Jhon" ,20)
#person2 = Person ("Jhon",20)

#person1.greet()
#person2.greet()

#class Student:
 #   school_name = "Digital school"

#student1 = Student()

#print(student1.school_name)

#class Student:
 #school_name = "Digital school"

 #def __init__(self, name, age):
    # self.name = name
  #   self.age = age
 #    self.course = course

#studenti1 = Student("Rion",16,"Python")
#studenti2 = Student("Rion",16,"Python")

#print(studenti1.course)
#print(studenti2.course)


#class MyClass:
 #   def __init__(self):
  #      self.__privat_variable = "this is a private variable"
      #self.public_variable = "This is a public variable"


   ##    print("This is a private method")

#my_class = MyClass()#instanca
#print(my_class.__privat_variable)

#my_class.__privat_method()


class MyClass:
    def __init__(self):
        self._protected_variable = "Hello World"

    def _protected_method(self):
        print("Protected method")


my_class = MyClass()
print(my_class._protected_variable())
#print(my_class._protected_method())

my_class._protected_method()

