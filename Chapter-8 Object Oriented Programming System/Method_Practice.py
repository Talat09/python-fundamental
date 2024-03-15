"""
Create student class that takes name and marks of 3 subjects as arguments in constructor.

Then create a method to print the average of the marks.
"""
class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def average(self):
        return (self.marks1+self.marks2+self.marks3)/3
    
s1=Student("Talat Mahmud",80,90,95)
print("Average of Three Subjects Marks:",s1.average())
print(s1.name,s1.marks1,s1.marks2,s1.marks3)

#another way to solve
class Marks:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
            sum=0
            for mark in self.marks:
                sum+=mark
            print("Average of Marks:",sum/3)
        
student=Marks("Talat Mahmud",[60,85,90])
student.get_avg()
      
        