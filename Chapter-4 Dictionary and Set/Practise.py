#Let't Practice

"""
1. store following word meanings in a dictionary:
table:"a piece of furniture", "list of facts & figures"
cat:"a small animal"

2.You are given a list of subjects for students.Assume one Classroom is required for 1 subjects.How many classroom are needed by all students?

'python','java','c++','c#','html','css','javascript','jquery','java'




3. Write a program to enter marks of 3 subjects from the user and store them in a dictionary.start with an empty dictionary and add one by one.Use subject name as key and marks as value.

5. Figure out a way to store 9 & 9.0 as separate values in the set.(You can take help of built in data types)
"""
#1 no problem solve
dictionary={
"cat":"a small animal",
"table":["a piece of furniture","list of facts & figures"],
 }
print(dictionary)
#2 no problem solve
subjects={"python","java","C++","python","javascript","java","python","java","C++","C"}
print("total classroom:",len(subjects))
#3 no problem solve
# marks { math:98,physics:88,english:75}
marks={}
FirstSubject=int(input("enter first subject:"))
marks.update({"Physics":FirstSubject})
print(marks)
secondSubject=int(input("enter second subject:"))
marks.update({"Math":secondSubject})
print(marks)
thirdSubject=int(input("enter third subject:"))
marks.update({"English":thirdSubject})
print(marks)
#4 no problem solve
values={6,'6.0'}
print(values)
#4 no problem another way to solve
values1={
    ('float',6.0),
    ('int',6),
}
print(values1)