"""
Object Oriented Programming languages has 4 pillars:
1. Abstraction
2. Encapsulation
3. Inheritance
4.Polymorphism
"""
#Abstraction:
"""
Hiding the implementation details of a class and only showing the essential features to the user.
"""
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
         self.brk=True
         self.clutch=True
         print("car started...")

car1=Car()
car1.start()
#Encapsulation:
"""
wrapping data and functions into a single unit(object).
"""