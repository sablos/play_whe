import random

again = "y"
limit = 10
# score tracking variables
score = 0

# main game loop
while again == "y":
    # generate random winning number
    win_number = random.randint(1, limit)
    # skip a line here
    print()

    # ask user for first guess
    valid = False
    while not valid:
        guess = input(f"Guess the lucky number (between 1 and {limit}): ")
        if guess.isnumeric():
            num_guess = int(guess)
            if num_guess in range(1, limit + 1):
                valid = True

    if win_number == num_guess:
        print("Awesome! You nailed it on the first try!")
        score += 5
    elif num_guess > win_number:
        print("That's not it. Guess lower this time.")
    else:
        print("That's not it. Guess higher this time.")

    # give the player a second chance if they didn't get the first guess
    if num_guess != win_number:
        valid = False
        while not valid:
            guess = input(f"Guess again: ")
            if guess.isnumeric():
                num_guess = int(guess)
                if num_guess in range(1, limit + 1):
                    valid = True
        if num_guess == win_number:
            score += 3
            print("You got it! Good job!")
        elif num_guess > win_number:
            print("That's still not it. Guess a bit lower.")
        else:
            print("That's still not it. Guess a bit higher.")

    if num_guess != win_number:
        valid = False
        while not valid:
            guess = input(f"Last guess: ")
            if guess.isnumeric():
                num_guess = int(guess)
                # we can never get a value error here because we know guess is numeric
                if num_guess in range(1, limit + 1):
                    valid = True
        if num_guess == win_number:
            score += 1
            print("Finally you got it right!")
        else:
            print(f"Wrong! The winning number was {win_number}.")

    print(f"Score: {score}")
    # skip line
    print()
    again = input("Play again? (y/n): ")
