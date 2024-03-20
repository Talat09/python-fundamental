"""
Machine Generate a random number between 1 and 100
Suppose random number is 50 -->target number.

Then ask the user to guess the number.

If user guessed the number correctly, print "Congratulations! You guessed the number correctly."

If user guessed the number incorrectly, print "Sorry, you guessed the number less than target number."

If user guessed number greater than target number, print "Sorry, you guessed the number greater than target number."
"""
import random
target=random.randint(1,100)
while True:
   
    userChoice=input("Guess the Number or Quit(Q):")
   
    if userChoice=="Q":
        break
    userChoice=int(userChoice)
    if userChoice==target:
        print("Success! You guessed the number correctly.")
        break
    elif userChoice<target:
        print("Sorry, you guessed the number less than target number.")
    else :
        print("Sorry, you guessed the number greater than target number.")
print("-------GAME OVER-------")