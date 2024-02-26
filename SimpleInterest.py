#calculate simple interest

principle=float(input("Enter principle amount: "))
rate=float(input("Enter rate of interest: "))
time=float(input("Enter time period: "))
simple_interest=principle*rate*time/100
print("Simple interest is:",simple_interest)