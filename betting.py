import random

again = "y"
limit = 10
# score tracking variables
score = 0


def get_valid_number(prompt):
    guess = input(prompt)
    valid = False
    while not valid:
        if guess.isnumeric() and int(guess) in range(1, limit + 1):
            valid = True
        else:
            guess = input(f"Your guess must be between 1 and {limit}: ")
    return int(guess)


# main game loop
while again == "y":
    # generate random winning number
    win_number = random.randint(1, limit)
    # skip a line here
    print()

    # ask user for first guess
    num_guess = get_valid_number(f"Guess the lucky number (between 1 and {limit}): ")

    if win_number == num_guess:
        print("Awesome! You nailed it on the first try!")
        score += 5
    elif num_guess > win_number:
        print("That's not it. Guess lower this time.")
    else:
        print("That's not it. Guess higher this time.")

    # give the player a second chance if they didn't get the first guess
    if num_guess != win_number:
        num_guess = get_valid_number("Second chance: ")

        if num_guess == win_number:
            score += 3
            print("You got it! Good job!")
        elif num_guess > win_number:
            print("That's still not it. Guess a bit lower.")
        else:
            print("That's still not it. Guess a bit higher.")

    # third and final chance
    if num_guess != win_number:
        num_guess = get_valid_number("Final guess: ")

        if num_guess == win_number:
            score += 1
            print("Finally you got it right!")
        else:
            print(f"Wrong! The winning number was {win_number}.")

    print(f"Score: {score}")
    # skip line
    print()
    again = input("Play again? (y/n): ")
