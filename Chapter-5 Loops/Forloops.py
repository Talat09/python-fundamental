#loops are used for sequential traversal.For traversing list,string,tuples etc
#syntax
"""
For loops
for el in list:
    do something
"""
list =[1,2,3,]
for el in list:
    el=el+4 # add 4 to each element
    print("element:",el)

vegetables =["tomato","potato","onion","carrot"]
for vegetable in vegetables:
    print("vegetable:",vegetable)    

tuples=("potato","onion","carrot")
for tuple in tuples:
    print("tuple:",tuple)

#words
words='hello world'
for char in words:
    print("word:",char)

#if we need a task after loop execution then we use optional else
str='hello world'
for char in str:
    if char=='o':
        print("O found:")
        break
    print("char:",char)
else:
    print("End of Loop")#else not execute in break case