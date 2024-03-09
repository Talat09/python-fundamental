#1. print number from 1 to 100
for i in range(1,101):
    print(i)
#2. print number from 100 to 1
    for i in range(100,0,-1):
        print(i)
#3. print the multiplication table of a number n
n=int(input("Enter a number:"))
for i in range(1,11):
        print(n,"X",i,"=",n*i)