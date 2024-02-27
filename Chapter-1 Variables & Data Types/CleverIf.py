#Conditional Statement
#Clever If/Ternary Operator
#<var>=(false_val,true_val)[<condition>]
age=int(input("Enter your age: "))
vote=("false","true")[age>=18]
print("You are eligible to vote?",vote)

#salary wise tax percentage program
sal=float(input("Enter your salary: "))
tax=sal*(0.1,0.2)[sal>=5000]
print("Your tax percentage is:",tax)
