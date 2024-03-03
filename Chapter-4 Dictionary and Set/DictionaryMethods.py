#Dictionary Methods
myInfo={
    "name":"Talat mahmud",
    "subject":["Python","Javascript"],#list
    "topics":("list","dictionary","tuple",6),#tuples
    "age":23,#integer
    "is_working":True,#boolean
    "marks":94.4,#float
}
print(myInfo.keys())#return only the all keys
print(myInfo.values())#return only the all values
print(myInfo.items())#return all key:value pairs
pairs=list(myInfo.items())#convert to list
print("pairs:",pairs[1])
print(myInfo.get("name"))#return the value of the key
print(myInfo.get("address"))#return None
#type casting another data types
print(list(myInfo.keys()))#return the keys in list
new_dict={
    "name":"KL Rahim",
    "age":26,
}
myInfo.update(new_dict)#return the value of the key or Not found
print("new_update_info:",myInfo)
#print (myInfo["name2"]))  --> return error
#print (myInfo.get("name2")) -->No error return None