#Dictionary in Python
#Dictionary are used to store data values in key:value pairs

#They are unordered,mutable(Changeable) and don't allow duplicate keys
#variable_name={"key":value pairs}
#all data types are acceptable in dictionary
#dictionary data type
info={
    "name":"Talat mahmud",
    "subject":["Python","Javascript"],#list
    "topics":("list","dictionary","tuple",6),#tuples
    "age":23,#integer
    "is_working":True,#boolean
    "marks":94.4,#float
}
print(type(info))
#print our info dictionary
print(info)
#no indexing in dictionary data types
#how to access dictionary given below:
# print ( info[keys_name])
print(info["name"])
#if we use wrong key name then we get key error

#if we reassign a value to the key then it will change the value
info["name"]="Amir Hamja"

print(info["name"])
# add a new key and value in dictionary
info["address"]="Halishahar"
print(info)

#create a null/empty dictionary then assign key pair value
null_dict={

}
print("Null dict:",null_dict)
null_dict["name"]="Salma Dihan"
null_dict["age"]=23
null_dict["is_working"]=True
null_dict["marks"]=94.4
null_dict["address"]="X bazar"
null_dict["subject"]=["Python","Javascript"]
null_dict["topics"]=("list","dictionary","tuple",6)
print("Null dict:",null_dict)