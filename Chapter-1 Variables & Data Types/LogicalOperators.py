#Logical Operators (not,and,or)
#it works on boolean value (True or False)

#not operator
Rain=True
Sunny=False
NotRain=not Rain
NotSunny=not Sunny
print("Rain:",NotRain)#False
print("Sunny:",NotSunny)#True
a=50
b=30
c=(not (a>b))# a>b is true but when we use not it becomes false
print("c:",c)#False

#and operator
val1=True
val2=True
print("And Operator:",val1 and val2)#True when both are true
num1=True
num2=False
print("Another And Operator:",num1 and num2)#False when one of them is false

#or operator
Cloudy=True
Rainy=False
print("Or Operator:",Cloudy or Rainy)#True when one of them is true
num3=False
num4=False
print("Another Or Operator:",num3 or num4)#False when both are false
print("Another Or Operator with expression:", (a==b) or (a>b))# a is not equal to b(False) but a is greater than b(True) we know if one of them is true then it will be true