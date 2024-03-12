#Types of Functions
#1. Built-in Functions
"""
print()
len()
type()
range()
"""
print("Hello World","Talat Mahmud")#separator=" "
print("Hello World")#separator=":"
print("Talat Mahmud")#end="\n"
print("AMIR", end=" ")
print("HAMJA")
#2. User-defined Functions
"""
which program write by user
"""

#Default parameter->Assigning a default value to parameter,which is used when no argument is passed.
#default arguments always must be at the end of the parameter list.(b=1)
#calculate multiplication
def multiply(a,b=1):
    print(a*b)
    return a*b

multiply(2)

