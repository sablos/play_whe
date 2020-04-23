import random

win_number = random.randint(1, 3)

guess = int(input("Guess the lucky number (between 1 and 3): "))
print(f"The lucky number is {win_number}")
if guess == win_number:
    print("you won!")
else:
    print("You lost!")
