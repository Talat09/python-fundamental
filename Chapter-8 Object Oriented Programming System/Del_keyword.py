#used to delete object properties or object itself
class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks


student1=student("Raj",20,90)
print("Name:",student1.name,"Age:",student1.age,"Marks:",student1.marks)
del student1.name #deletes the name property
print("Name:",student1.name,"Age:",student1.age,"Marks:",student1.marks)