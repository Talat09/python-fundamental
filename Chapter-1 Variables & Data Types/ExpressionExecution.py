#string & Numeric values can operate together with *
A,B = 2,3
txt = "@"
print("Expression Execution:",A*txt*B)
#String & String can operate with +   join/concatenation string with +

C,D="2",3
Txt = "@"
print((C+Txt)*D)
#Numeric values can operate with all arithmetic operator
E,F=2,3
G=4
print(E+F*G)

#Arithmetic expression with integer and float will result in float
H,I=10,5.0
J=H*I
print(J)

#Result of division operator with two integers will be float
Talat,Dihan=1,2
Nuhan=Talat/Dihan
print(Nuhan)

#Integer division with float and int will give int displayed as float
# // Integer division 
sanjida,joy=1.5,3
susmi=sanjida//joy
print(susmi,sanjida/joy)

# floor gives closest integer,which is lesser than or equal to the float value 
#Result of(A//B) is same as floor (A/B)



#Remainder is negative when denominator is negative
#(5%+2)=7  +ve
#(-5%-2)=7  +ve
#(5%-2)=-3 -ve
#(-5%2)=3 +ve
ami=5
tmi=-2
print("modulo",5%2)
print(-5 % -2)
print("ami tmi:",ami%tmi)
print(-5%2)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#single line comment


"""This is
multiline comment
"""