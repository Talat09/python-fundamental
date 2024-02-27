#1.Write a program to input 2 numbers and print their sum.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum=num1+num2
print("Sum of",num1,"and",num2,"is:",sum)
#2.write a program input side of a square and print its area.
side=float(input("Enter side of square: "))
area =side*side
print("Area of square with side",side,"is:",area)

#3.write a program to input 2 floating numbers and print their average
num3=float(input("Enter your first float number:"))
num4=float(input("Enter your second float number:"))
avg=(num3+num4)/2
print("Average of",num3,"and",num4,"is:",avg)

#4.write a program to input 2 integers,a and b
#Print True if a is greater than or equal to b,if not print False
a=int(input("Enter first integer: "))
b=int(input("Enter second integer: "))
if a>=b:
    print("True")#a is greater than b that why it is True
else:
    print("False")#a is less than b that why it is False