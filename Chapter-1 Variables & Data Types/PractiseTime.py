#Print Output for: 
#A = 5 & G=M   ---> Fee is 300
# A = 2 & G=F  ---> Fee is 200
"""
AND Operator
TT=T
FT=F
TF=F
FF=F


OR Operator
TT=T
TF=T
FT=T
FF=F
"""
A=int(input("Enter A: "))
G=input("Enter M/F: ")
if(A==1 or A==2) and  G=="M":
    print("fee is 100")
elif(A==3 or A==4) or  G=="F":
    print("fee is 200")
elif(A==5  and  G=="M"):
    print("fee is 300")
else:
    print("no fee")