#string Functions
str="i am coder"
subStr=str.endswith("er")#returns true if string ends with substr
print(subStr)
#Capitalize 1st character of string
str1="i am coder"
capitalizeFirstChar=str1.capitalize()
print(capitalizeFirstChar)
print(capitalizeFirstChar)
# Replace all occurrence of old with new
oldStr="i am coder"
newStr=oldStr.replace("i","a") #(old,new)
print(newStr)# i replaced with a output: a am coder
oldStr1="i am javascript coder"
newStr1=oldStr1.replace("javascript","python")
print(newStr1)# javascript replaced with python output: i am python coder

#find() function
word="python is awesome"
findO=word.find("o")
print(findO)#here first o index position return 
findOagain=word.find("q")
print(findOagain) # here return -1 because -1 not valid its can't find q in this word string

#count() function
word1="Talat is a web developer.Also he is a Computer science student"
countWord=word1.count("is")
print(countWord)#it returns 2 because here (is )are 2 times present

