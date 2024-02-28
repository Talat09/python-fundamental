#List in python
"""
A build-in data type that stores set of values
it can store elements of different data types(int,float,string,boolean)
"""
#lets create a list
marks=[95.8,77.2,44.5,40.8,50.9]
print(marks)
print(type(marks))
#lets access the elements of the list
print(marks[0])
#python can store different kind of data types in one list which javascript can not
student=["Talat",95.8,"Chittagong"]
print(student)

"""
sting in python -->immutable means not changeable
list in python -->mutable means changeable
"""
str="Talat"
print(str[0])
# str[0]="Hello"#its not allowed to change

#list
student[0]="Salma Fariha Juhi"#list change allowed
print(student)

#Slicing is possible in the list
#list_name[starting_index:ending_index]
slicingList=student[0:2]
print(slicingList)#['Salma Fariha Juhi', 95.8]
