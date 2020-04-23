import random

again = "y"
# score tracking variables
wins = losses = 0

while again == "y":
    win_number = random.randint(1, 3)
    # skip a line here
    print()
    guess = int(input("Guess the lucky number (between 1 and 3): "))
    print(f"The lucky number is {win_number}")
    if guess == win_number:
        print("you won!")
        wins += 1
    else:
        print("You lost!")
        losses += 1
    print(f"Score: wins {wins}, losses {losses}")
    # skip line
    print()
    again = input("Play again? (y/n): ")
