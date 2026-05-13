import random

playing = True
number = str(random.randint(0, 9))

print("I will print a number 1 to 9 and you have to guess it one digit at a time")
print("The gme ends when you get a win!")

while playing:
    guess = input("Give me your best guess! \n")
    if number == guess :
        print("You won the game!, good job!")
        print("The number was", number)
    else:
        print("your guess isn't queit correct please try again \n")