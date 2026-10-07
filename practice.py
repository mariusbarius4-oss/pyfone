# plan
#
# computer saves random number as var
# user inputs number
# if number greater than or less than then tell user and loop until correct

import random

x =(random.randint(1, 50))

print(x) # DEBUG

guessed = False

while guessed == False:
    numberguessed = int(input("guess the number\n"))

    if numberguessed < x:
        print("real number is less than guessed number")

    elif numberguessed > x:
        print("real number is more than guessed number")

    else:
        print("ur right")
        guessed = True