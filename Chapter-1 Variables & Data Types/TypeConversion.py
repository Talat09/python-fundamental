#Python have two types of Type Conversion
# 1. Implicit/automatic --> Python automatically converts one data type to another data type.
a=5
b=3.25
sum=a+b
print(sum)#here python automatically converts 5 integer to float 5.00

# 2. Explicit/casting --> You have to explicitly/manually convert one data type to another data type.
c=5
d="3"
sum1=c+int(d)
print(sum1)#here python converts b ="3" string to integer value 3 and then adds it to a integer value 5
#python can not convert character to integer or float
e="Talat"
f=5
sum2=e+f
print(sum2)
#here python gives error because python can not convert character to integer or float 
#Through error:TypeError: can only concatenate str (not "int") to str

#python can convert integer to sting
age = 50
print(str(age))#here python converts integer value 50 to string '50'