#Class method
"""
A class method is bound to the class and receives the class as an implicit first argument.

Note:- Static method can't access or modify class state and generally for utility.


class Student:
    @classmethod
    def college(cls):
        pass
"""
class Person:
    name="anonymous"

    def ChangeName(self,name):
        Person.name=name #to change class attribute
        # self.name=name



person1=Person()
person1.ChangeName("John Mallik")
print("Name From Object Attribute:",person1.name)
print("Name From Class Attribute:",Person.name)
class Person_T:
    name="anonymous"

    def ChangeName(self,name):
       self.__class__.name=name #to change class attribute



person_T1=Person_T()
person_T1.ChangeName("John Mallik")
print("Name From Object Attribute:",person_T1.name)
print("Name From Class Attribute:",Person_T.name)

#another way to write class method
class Car:
    color="Red"
    @classmethod
    def ChangeColor(cls,color):
        cls.color=color

car1=Car()
car1.ChangeColor("Blue")
print(car1.color)
print(Car.color)