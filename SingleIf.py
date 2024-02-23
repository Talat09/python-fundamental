#Conditional Statement
#single if/Ternary operator
#<var>=<val1> if <condition> else <val2>
food=input("Enter your food preference: ")
eat="yes" if food=="cake" else "no"
print("Do you like to eat cake? ",eat)

#<statement1> if <condition> else <statement2>
food=input("Food: ")
print("sweet") if food=="cake" or food=="jilapi" else print("no sweet")