#write a program to input user's first name & print its length
users_first_name=input("Enter users first name: ")
print(len(users_first_name))


#write a program to find occurrence of '$' in a string
str="Talat$Mahmu$d$"
print(str.count("$"))

#write a program to check if a number entered by the user is odd or even
number=int(input("Enter a number: "))
if number%2==0:
    print("This number is even")
else:
    print("This number is odd")


#write a program to find the greatest of 3 numbers entered by the user
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if num1>num2 and num1>num3:
    print("The greatest number is:",num1)
elif num2>num1 and num2>num3:
     print("The greatest number is:",num2)
else:
    print("The greatest number is:",num3)


#Nesting if else conditional statement
age=85
if age>=18:
    if age>=70:
        print("You are not eligible to drive")
    else:
        print("You are  eligible to drive")
else:
    print("You are not eligible to drive")


