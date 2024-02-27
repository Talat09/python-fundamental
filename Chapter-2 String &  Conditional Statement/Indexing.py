#Every character got a position which is called indexing

#Talat_Mahmud
#01234567891011
str1="Talat_Mahmud"
#Indexing helps us to access a character in a string 
ch1=str1[0]# 0 index T
ch2=str1[1] # 1 index a
ch3=str1[2] # 2 index l
ch4=str1[3] # 3 index a
ch5=str1[4] # 4 index t

print(ch1,ch2,ch3,ch4,ch5)

#If we want to assign a character replaced by another character then we can not use indexing
#with the help of indexing we access it position but we never manipulate its value
str2="Talat_Mahmud"
str2[0]="M"#Its not allowed to manipulate string with indexing
print(str2)#TypeError: 'str' object does not support item assignment