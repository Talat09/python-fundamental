"""
Class.attribute
object.attribute

if one data same for all object then we can define it in class.not define into the constructor.

Object attribute get higher priority over class attribute.
"""
class Student:
    university_name="East Delta University"#class attribute
    name="anonymous"#class attribute
    def __init__(self,name,id,course):
        self.name=name #object attribute
        self.id=id #object attribute
        self.course=course #object attribute

student1=Student("Tawfik Reza Rafy",181008212,"Algorithm")

student2=Student("Talat Mahmud",181008312,"Database Management System")

student3=Student("Joyjit Chowdhury",181008512,"Computer Network")

print(student1.university_name,"\n",student1.name,"\n",student1.id,"\n",student1.course)

print(student2.university_name,"\n",student2.name,"\n",student2.id,"\n",student2.course)

print(student3.university_name,"\n",student3.name,"\n",student3.id,"\n",student3.course)