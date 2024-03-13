"""
Constructor: (__init__ Function is called constructor)
All classes have a function called __init__,which is always executed when the object is being initiated.
"""

#creating Class
#constructor by default takes self parameter(its one kind of this key word which is used in js)
#self parameter is a reference

"""
class Student:
    #Default Constructor
    def __init__(self):
       pass
    #parameterized Constructor
    def __init__(self,name,marks):
        # print(self)
        self.name=name #name is a attributes
        self.age=age#age is a attributes

       
"""
class Student:
 
    def __init__(self,name,age):
        # print(self)
        self.name=name #name is a attributes
        self.age=age#age is a attributes

        print("This is constructor For creating new student")


#Student() its an instance
s1=Student("Adib Ahmed",18)#when create object its called automatically constructor self

print("Name:",s1.name,"Age:",s1.age)#Adib Ahmed


s2=Student("Amin Hossain",20)
print("Name:",s2.name,"Age:",s2.age)#Amin Hossain

"""
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
"""