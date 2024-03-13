#Object Oriented Programming in python

"""
To map with real world scenarios, we started using objects in code.This is called Object Oriented Programming.
""" 
#Class and Objects in python:
#Class is a blueprint for creating objects

#Let't create a student class
"""
class class_name:
    attribute_name=value
    attribute_name=value
"""
class Student:
    name="Talat Mahmud"
    age=20


#creating Object (instance)
    
"""
object_name=class_name()

"""
student1=Student()
print(student1.name)

#Car Factory Example:
class Car:
    color="Red"
    brand="BMW"

car1=Car()
print("Color:",car1.color,",","Brand:",car1.brand)