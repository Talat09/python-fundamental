"""
Create a new file "practice.txt" using python.Add the following data in it.

Hi everyone
we are learning File I/O
using python
I like programming in python


Write a program that replace all occurrences of "python" with "java" in the above file.



"""
with open("practice.txt","w") as file:
    file.write("Hi everyone\n")
    file.write("we are learning File I/O\n")
    file.write("using python\nI like programming in python")
with open("practice.txt","r") as file:
   data = file.read()
new_data=data.replace("python","java")
print(new_data)
with open("practice.txt","w") as file:
    file.write(new_data)

"""
Search if the word "learning" exists in the file or not.
"""
def search_word():
    word="learning"
    with open("practice.txt","r") as file:
        data = file.read()
        if data.find(word) != -1:
            print("word exists")
        else:
            print("word doesn't exists")

search_word()

"""
From a file containing numbers separate by comma,print the count of even numbers.
"""
def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
       while data:
           data=f.readline()
           if word in data:
               print("line_no:",line_no)
               return
           line_no +=1
    return -1

check_for_line()

with open("practice.txt","r") as f:
    data=f.read()
    print(data)
#individual number
    num=""
    for i in range(len(data)):
        if data[i]==",":
            print(int(num))
            num=""
            
        else:
           num+=data[i]
#parse integer value
           
#another method
count=0
with open("practice.txt","r") as f:
    data=f.read()

    nums=data.split(",")
    for val in nums:
        if int(val)%2==0:
            count += 1
print(count)