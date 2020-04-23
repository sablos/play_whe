import random

again = "y"
limit = 3
# score tracking variables
wins = losses = 0

while again == "y":
    win_number = random.randint(1, limit)
    # skip a line here
    print()
    valid = False
    while not valid:
        guess = input(f"Guess the lucky number (between 1 and {limit}): ")
        if guess.isnumeric():
            num_guess = int(guess)
            # we can never get a value error here because we know guess is numeric
            if num_guess in range(1, limit + 1):
                valid = True
    print(f"The lucky number is {win_number}")
    if win_number == num_guess:
        print("You won!")
        wins += 1
    else:
        print("You lost!")
        losses += 1
    print(f"Score: wins {wins}, losses {losses}")
    # skip line
    print()
    again = input("Play again? (y/n): ")
