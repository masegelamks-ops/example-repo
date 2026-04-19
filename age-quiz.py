# This program takes the users age and gives feedback related to the age

age = int(input("Insert your age "))
if age > 100:
    print("Sorry you are dead")
elif age > 65:
    print("Enjoy your retirement")
elif age > 40:
    print ("You're over the hill")
elif age == 21:
    print ("Congrants on your 21st")
elif age <13:
    print("You qualify for a kiddie discount")
else:
    print("Age is but a number")