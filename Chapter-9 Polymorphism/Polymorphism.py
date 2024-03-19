#Polymorphism : Operator overloading

"""
When the same operator is allowed to have different meaning  according to the context.


Operator and Dunder function:
a+b # addition
a-b # subtraction
a*b # multiplication
a/b # division
a//b # floor division
a%b # modulus
Home work:
@getter
@setter
"""
#Overloading  --> change the meaning of operator
print(1+2)
print("Rahul" + "Dev") #concatenate
print([1,2,3]+[4,5,6]) #merge

#create complex number for complex class because python have no complex number class

class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    
    def showNumber(self):
        print(self.real,"i +",self.imaginary,"j")
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImaginary=self.imaginary+num2.imaginary
        return Complex(newReal,newImaginary)
    def __sub__(self,num2):
        newReal=self.real-num2.real
        newImaginary=self.imaginary-num2.imaginary
        return Complex(newReal,newImaginary)
num1=Complex(1,3)
num1.showNumber()
num2=Complex(3,4)
num2.showNumber()
num3=num1+num2
num4=num1-num2
num3.showNumber()
num4.showNumber()