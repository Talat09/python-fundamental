""""
if-elif-else(SYNTAX)
if(condition):
statement1
elif(condition):
statement2
else:
statementN
"""
#Python is INDENTATION(proper spacing) BASED PROGRAMMING LANGUAGE after if line it takes 4space
#if your age is greater than equal 18 then you are eligible to vote otherwise you are not eligible to vote
age=18
if(age>=18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

"""
Traffic Light Example
Red:"stop"
Yellow:"Look"
Green:"Go"
Blue or white:"light is broken"
"""

light=input("Enter Color: ")
if(light=="red"):
    print("stop")
elif(light=="green"):
        print("Go")
elif(light=="yellow"):
     print("Look")
else:
     print("light is broken")



