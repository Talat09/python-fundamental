#1. Print numbers from 1 to 100
number=1
while number<=100:
    print(number)
    number+=1

#2. print numbers from 100 to 1
number1=100
while number1>=1:
    print(number1)
    number1-=1

#3. print the multiplication table of a number n
n=3
i=1
while i<=10:
    print(n,"X",i,"=",n*i)
    i+=1

#4. print the elements of the following list using loop:
list=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(list):
    print("Element Of the List:",list[i])
    i+=1

#5. print for a number x in this tuple using loop:
    
tuple=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i<len(tuple):
    if x==tuple[i]:
        print("Element Found index of:",i)   
    else:
        print("Element Not Found")
 
    i+=1

#Break: used to terminate or exit the loop when encountered
#Continue:terminates execution in the current iteration and continues execution of the loop with the next iteration
    
A=1
while A<=10:
    print("A:",A)
    if A==5:
        print("Breaking Loop")
        break
    A+=1
print("End of Loop")

B=1
while B<=10:
   
    if B==5:
        B+=1
        continue#skip iteration and go to next iteration
    print("B:",B)
    B+=1