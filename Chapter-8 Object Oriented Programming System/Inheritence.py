#Inheritance
"""
When one class (child/derived) derives the properties and methods of another class(parent/base).

class Car:
    .....


class BMWCar(Car):
        ......
"""
#Example of single inheritance
class Car:
    color="Red"
    @staticmethod
    def start():
        print("Car started..")
    @staticmethod
    def stop():
        print("Car stopped!")

class BMWCar(Car):
    def __init__ (self,name):
        self.name=name

car1=BMWCar("BMW fortune")
car2=BMWCar("BMW Luis")
car1.start()
car2.stop()
print(car1.color)

#we categories inheritance in 3 types
#1.Single Inheritance
#2.Multi-level Inheritance
#3.Multiple Inheritance



#Example of Multi-level Inheritance
class Book:
    cover="Black"
    @staticmethod
    def start():
        print("This book is Authored by..")
   
class MyBook(Book):
    def __init__ (self,name):
        self.name=name

class Print_Book(MyBook):
    def __init__ (self,name,genre):
        self.name=name
        self.genre=genre
        

book1=Print_Book("Python","Thriller")
print("Cover_Color:",book1.cover,",","Book_Name:",book1.name,",","Book_Genre:",book1.genre)
book1.start()
#3.Example of Multiple Inheritance
class A:
    varA="welcome to class A"

class B:
    varB="welcome to class B"
class C(A,B):
    varC="welcome to class C"

c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)