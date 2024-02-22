#University grading system

#93 & above A
#89 &  <93 A-
#86 & <89 B+
#82 & <86 B
#79 & <82 B-
#75 & <79 C+
#72 & <75 C
#69 & <72 C-
#65 & <69 D+
#60 & <65 D
#below <59 F
mark=int(input("Enter your mark: "))
if(mark>=93):
     print("A")
elif(mark>=89 and mark<93):
     print("A-")
elif(mark>=86 and mark<89):
     print("B+")
elif(mark>=82 and mark<86):
     print("B")
elif(mark>=79 and mark<82):
     print("B-")
elif(mark>=75 and mark<79):
     print("C+")
elif(mark>=72 and mark<75):
     print("C")
elif(mark>=69 and mark<72):
     print("C-")
elif(mark>=65 and mark<69):
     print("D+")
elif(mark>=60 and mark<65):
     print("D")
else:
     print("F")