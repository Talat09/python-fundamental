#1. write a recursive function to calculate the sum of first n natural numbers
def sum_of_n(n):
    if n==0:
        return 0
    return n+sum_of_n(n-1)

print(sum_of_n(10))
"""
sum_of_n(10)=10
sum_of_n(9)=9
sum_of_n(8)=8
sum_of_n(7)=7
sum_of_n(6)=6
sum_of_n(5)=5
sum_of_n(4)=4
sum_of_n(3)=3
sum_of_n(2)=2
sum_of_n(1)=1
//
sum_of_n(10)=45+10=55
sum_of_n(9)=36+9=45
sum_of_n(8)=28+8=36
sum_of_n(7)=21+7=28
sum_of_n(6)=15+6=21
sum_of_n(5)=10+5=15
sum_of_n(4)=6+4=10
sum_of_n(3)=3+3=6
sum_of_n(2)=1+2=3
sum_of_n(1)=1
"""
#2. write a recursive function to print all element in a list
def print_list(list,idx=0):
    if idx==len(list):
        return 
    print(list[idx]) 
    # 0==4? no 
    # 1==4? no 
    # 2==4? no
    # 3==4? yes
    
    print_list(list,idx+1)    
#thats why 1st element print and increase idx value 1
#thats why 2nd element print and increase idx value 1
#thats why 3rd element print and increase idx value 1
#thats why 4rth element print and increase idx value 1
fruits=["banana","orange","apple","mango"]
print_list(fruits,0)