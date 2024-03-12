#Recursion

"""
when a function calls itself repeatedly
"""
#using loop
def recursion(number):
    i=number
    n=1
    while i>=n:
        print("i=",i,"n=",n)
        i-=1

print(recursion(10))

#using recursion->recursive function
def show(number):
    if(number==0):#base case decide recursion stop or not
        return
    print(number)
    show(number-1)
    print("End")
show(5)# 5, 4=n-1, 3=n-2, 2=n-3, 1
"""
show(n=5)->5
show(n=4)->4
show(n=3)->3
show(n=2)->2
show(n=1)->1
"""

#Recursion Practice
#returns n!
"""
n!=n*(n-1)!
5!=5*(4)!
5!=5*(4*3*2*1)
"""
def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)
   
print(factorial(6))