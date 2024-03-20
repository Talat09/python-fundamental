import random
import string

pass_length=32
charValues=string.ascii_letters+string.digits+string.punctuation
print(charValues)
"""
List comprehension
result = ''.join([random.choice(charValues) for i in range(pass_length)])
print(result)
"""
password=""
for i in range(pass_length):
    # print("i:",i)
    password=password+random.choice(charValues)
    print("target:",password)

print("Your Random Password is:",password)