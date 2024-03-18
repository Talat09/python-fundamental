"""
Private attributes and methods are meant to be used only within the class and are not accessible from outside the class.


if you want to make a private attribute or method, you can use __double underscore__ before the attribute or method name.
"""
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass#private attribute
    def reset_pass(self):
        print("pass:",self.__acc_pass)


a1=Account(181008212,'tady@eret')

print("Account_Number:",a1.acc_no,",","Password:",a1.reset_pass())
class Person:
    __name="anonymous"
    def __hello(self):#private method which is not access out of the class
        print("hello world")

    def welcome(self):
        self.__hello() #here we got not error because it access inside the class
p1=Person()
# p1.__hello()
# print(p1.__name)#error because its a private attribute
p1.welcome()
