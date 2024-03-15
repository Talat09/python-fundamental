#Methods are functions that belong to objects.

"""
Creating class:
class Student:
    def __init__(self,fullname):
        self.name=fullname 

    def hello(self):
        print("Hello",self.name)

Creating object:
s1=Student("Talat mahmud")

Calling object method:
s1.hello()
"""
class Car:
    def __init__(self,color,brand,milage):
        self.color=color
        self.brand=brand
        self.milage=milage

    def welcome(self):#method
        print("Welcome To The",self.brand,"Car Showroom")
    def get_milage(self):#method
        return self.milage
car1=Car("Red","BMW",20000)
car2=Car("Blue","Toyota",30000)
First_car_details=car1.color,car1.brand,car1.milage
Second_car_details=car2.color,car2.brand,car2.milage
car1.welcome()
print(car1.get_milage())
print(First_car_details)
car2.welcome()
print(Second_car_details)

