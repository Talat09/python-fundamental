#Methods that don't use the self parameter (work at class level)
"""
class Student:
    @staticmethod  #decorator
    def college():
    print("I am a college student")

* Decorator allow us to wrap another function in order to extend the behavior of the wrapped function, without without permanently modifying it.
*Decorator takes parameter as a function and returns output a function.
"""
class Student:
    @staticmethod #decorator
    def college():
        print("I am a college student")

s1 = Student()
s1.college()