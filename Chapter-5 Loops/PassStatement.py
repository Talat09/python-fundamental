#pass is a null statement that does nothing.It is used as a placeholder for future code.
"""
for el in range(10):
    pass
"""
for el in range(10):
    pass
print("Hello World")

#Lets Practice
#1. Write a program to find the sum of first n numbers
n=6
sum=0
for i in range(1,n+1):
    sum+=i
print("Total Sum:",sum)
#solved using while loop
#1. Write a program to find the sum of first n numbers
m=7
Total=0
i=1
while i<=m:
    Total+=i
    
    i+=1
print("Total Sum:",Total)
#2. Write a program to find the factorial of first n numbers
j=5
factorial=1
for i in range(1,j+1):
    factorial=factorial*i
print("Factorial:",factorial)
#solved using while loop
numbers=6
factorial1=1
x=1
while x<=numbers:
    factorial1=factorial1*x
    #step 1: 1=1*1
    #step 2: 1=1*2=2
    #step 3: 2=2*3=6
    #step 4: 6=6*4=24
    #step 5: 24=24*5=120
    #step 6: 120=120*6=720
    x+=1
print("Factorial1:",factorial1)