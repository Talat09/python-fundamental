#let's Practice

#write a program to ask the user to enter names of their 3 favorite movies & store them in a list

# FirstMovie=input("Enter your 1st favorite movies: ")
# SecondMovie=input("Enter your 2nd favorite movies: ")
# ThirdMovie=input("Enter your 3rd favorite movies: ")
# movies=[]
# movies.append(FirstMovie)
# movies.append(SecondMovie)
# movies.append(ThirdMovie)
# print(movies)

#another way
# Cinemas=[]
# Cinemas.append(input("Enter your 1st favorite cinema: "))
# Cinemas.append(input("Enter your 2nd favorite cinema: "))
# Cinemas.append(input("Enter your 3rd favorite cinema: "))
# print(Cinemas)

#Write a program to check if a list contains a palindrome(1st and last are same "maam") of elements.(Hint:Use copy() method)
list1 = [1,2,1]
list2=["a","b","h","i"]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("its palindrome")
else:
    print("its not palindrome")


#not palindrome
copy_list2=list2.copy()#[1,2,3]
copy_list2.reverse()#[3,2,1]
if(copy_list2==list2):
    print("its palindrome")
else:
    print("its not palindrome")
#copy and reverse then check with list is equal or not if equal then its palindrome


#write a program the number of students with the "A" grade in the following tuple

grades=("C","D","A","A","B","B","A")
AGradeStudent=grades.count("A")
print(AGradeStudent)

#store the above values in a list and sort them form A to D
grades_list=["C","D","A","A","B","B","A"]
grades_list.sort()
print(grades_list)