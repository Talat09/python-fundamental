#1. Print the elements of the following list using a loop:
elements=[1,4,9,16,25,36,49,64,81,100]
for element in elements:
    print("Element Of the List:",element)
#2. Search for a number x in this tuple using loop
#tuples
#this also called linear search
tuples=(1,4,9,16,25,36,49,64,81,100,49)
x=49
for tuple in tuples:
    if x==tuple:
        print("Element Found index of:",x)
    else:
        print("Element Not Found")