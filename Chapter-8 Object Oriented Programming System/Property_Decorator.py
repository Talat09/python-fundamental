#Property decorator --> we use @property decorator on any method in the class to use the method as a property.

"""
Let's imagine a scenario where a teacher give you the result when teacher recheck the student's result its changed 98 to 90
"""
class Student:
    def __init__(self,name,phy,chem,math):
        self.name=name
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy+self.chem+self.math)/3) + "%"

student1=Student("Rahul",98,97,99)
print("Result:",student1.percentage)

student1.phy=90
print("Changes Here:",student1.phy)
print("After Changes Result:",student1.percentage)#but here not change the percentage
"""
Let's try to solve this problem using property decorator
"""
class NewStudent():
    def __init__(self,name,phy,chem,math):
        self.name=name
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + "%"
    
new_student=NewStudent("Rahul",98,97,99)
print("Result:",new_student.percentage)

new_student.phy=90
print("Changes Here:",new_student.phy)
print("After Changes Result:",new_student.percentage)