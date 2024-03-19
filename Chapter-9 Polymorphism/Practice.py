"""
Question 1:
Define a Circle class to create a circle with radius r using constructor.
Define an Area method of the class which calculates the area of the circle.
Define a Perimeter method of the class which allows you to calculates the perimeter of the circle.
"""
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def Area(self):
        return 3.14*self.radius**2
    def Perimeter(self):
        return 2*3.14*self.radius
    
circle1=Circle(21)
print(circle1.Area())
print(circle1.Perimeter())

"""
Question 2:
Define a Employee class with attributes role,department and salary.This class also has showDetails() method.

Create an Engineer class that inherits properties from Employee and has additional attributes like name,age.
"""
class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    def showDetails(self):
        print("Role:",self.role)
        print("Department:",self.department)
        print("Salary:",self.salary)

class Engineer(Employee):
    def __init__(self,name,age,role,department,salary):
        super().__init__(role,department,salary)
        self.name=name
        self.age=age
    def showDetails(self):
        super().showDetails()
        print("Name:",self.name)
        print("Age:",self.age)

employee1=Engineer("Rahul",23,"Engineer","IT",100000)
employee1.showDetails()
"""
Question 3:
Create a class called Order which stores item and its price.
use Dunder function __gt__() to convey that:
Order1>Order2 if price of Order1 is greater than price of Order2.
"""
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,order2):
        return self.price>order2.price
    
order1=Order("Laptop",10000)
order2=Order("Mobile",5000)
print(order1>order2)#True because price of order1 is greater than price of order2