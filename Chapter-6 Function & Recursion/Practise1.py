#1. Write a program to print the length of a list(list is the parameter)
world_cities=["Amman","Irbid","Jerash","Cairo","London"]
bd_cities=["Dhaka","Chittagong","Khulna","Barishal","Rangpur"]

def print_cities(list1,list2):
   sum_cities=list1+list2
   return len(sum_cities)
    # print("Length of list:",length)

output=print_cities(world_cities,bd_cities)
print(output)
#2. write a program to print the element of a list in a single line.(list is the parameter)
print(world_cities[0],end=" ")
print(world_cities[1],end="\n")

def print_items(list):
    for i in list:
        print(i,end="\n")
    return i

print(print_items(world_cities))
print(print_items(bd_cities))

#3. write a program to find the factorial of n.

"""
n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)


//
def print_factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    return fact

print(print_factorial(5))
"""
def print_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact #return the value of the factorial
print(print_factorial(5))

#4. write a program convert USD to BDT
def convert_usd_to_bdt(usd):
    bdt=usd*110
    return bdt

print(convert_usd_to_bdt(100),"BDT")

#5. write a program to take input from user,if the number is odd return "odd" if even then print "even"
def odd_even(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
    
print("Your Number is ",odd_even(11))