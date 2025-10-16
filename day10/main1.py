class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @property
    def name(self):
        return  self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
         return self.__age
    @age.setter
    def age(self, age):
         self.__age = age

s = Student("John", 19)
print("Name of student",s.name)
print(" Age of student ",s.age)

s.name = "Deon"
s.age = 14
print("Update name  of student",s.name)
print("Update age of student ",s.age)

