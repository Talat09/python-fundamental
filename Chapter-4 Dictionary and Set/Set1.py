#set is mutable but set of elements are immutable
collection={1,2,3,4,'hello','world',}
print(collection)#set print unordered values
print(type(collection))
print(len(collection))
#set ignore duplicate value
collection2={1,2,3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5}
print(collection2)#here set ignore duplicate value

#collection={} this an empty dictionary not empty set
students=set()
students.add("Talat")
students.add("Mahmud")
students.add(1)
students.add(2)
print(students)#empty set
#remove 1 value from the set
students.remove(1)
#if we remove not exist value from the set it will return key error
# add a tuple
students.add(("rafy","sanjida",12,23))
#if we want to add a list then its trow an error which is typeerror unhashable type: 'list'
#students.add([1,3,4])
print(students)#empty set
print(type(students))

#if we clear the set it will remove all the values
students.clear()
print(students)#empty set
#another create set
information={'hello','salma','apnacollege'}
print(information)
#pop method used to remove a random value
information.pop()
information.pop()
print(information)


