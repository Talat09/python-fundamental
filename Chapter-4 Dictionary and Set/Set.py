#set in python
#set is the collection of the unordered items
#Each element in the set must be unique & immutable
#we can't set list and dictionary as set value because they are mutable
# boolean,integer,float,string and tuple are allowed in the set
nums={1,2,3,4,5}
print(nums) 
nums2={1,2,2,2} #repeated elements stored only once, so it resolved to {1,2}
print("nums2:",nums2)

#empty set syntax
# null_set=set()

set1={55,44}
#Set methods
set.add({"age":89})#adds an element
set.remove({"age":85})#removes the element from the set
set.clear()#clears the set
set.pop()#removes a random value


set.union(set1)#combines both set values and returns new
set.intersection(set1)#combines common values and returns new
