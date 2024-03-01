#Create tuples in python
#tuples are immutable it means they can not be changed
tup=()

#tup=(1,) if we don't use comma after 1 then python understand its an integer value not a tuple
print(tup)
#type print
print(type(tup))

tuples=(1,2,3,1,1)
print(tuples)

#slicing is possible in tuples
print("slicing",tuples[0:2])

#Tuple Methods
#Tuples have no append,insert,remove,pop,sort,reverse methods

#indexing is possible in tuple
#tuple.index(el)
print("indexing:",tuples.index(1))

#count number in tuple
print("count number in tuple:",tuples.count(1))#1 present in 3 time in tuples variable