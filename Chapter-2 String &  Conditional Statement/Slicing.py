#Accessing parts of a string which is called slicing

# variable_name[start_index:end_index] *ending index is not included when slicing

name="Talat Mahmud"
slicingTalat=name[0:5]
#slicingTalat=name[:5] python automatically detect its index start with 0
print(slicingTalat)
slicingMahmud=name[6:12]
#slicingMahmud=name[6:] python automatically detect its index end with last index
print(slicingMahmud)
addingTalatMahmud=slicingTalat+" "+slicingMahmud
print(addingTalatMahmud)
name1="Talat mahmud"
slicingMahmud1=name1[6:len(name1)]#another way slicing
print(slicingMahmud1)


#Negative Index
#Negative index is used to access a character from the end of the string to start
fruits="banana"
negativeIndexSlice=fruits[-3:-1]#negativeIndexSlice=fruits[-3:len(fruits)]
print(negativeIndexSlice)

