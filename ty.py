import random

again = "y"
wins = losses = 0
limit = 3

while again == "y":
    win_number = random.randint(1, limit)
    guess = int(input(f"Guess the lucky number (between 1 and {limit}): "))
    if guess == win_number:
        print("You won!")
        wins += 1
    else:
        print(f"You lose! The lucky number was {win_number}.")
        losses += 1
    print(f"\nScore: wins {wins}, losses {losses}\n")
    again = input("Play again? (y/n): ")