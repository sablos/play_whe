import random

limit = 10
# score tracking variables
score = 0


def get_valid_number(prompt, max):
    entry = input(prompt)
    valid = False
    while not valid:
        if entry.isnumeric() and int(entry) in range(1, max + 1):
            valid = True
        else:
            entry = input(f"Your entry must be between 1 and {max}: ")
    return int(entry)


print("Hello! Welcome to \"Guess The Number\"! Test your psychic abilities!")
rounds = get_valid_number("How many games would you like to play (up to 100)?: ", 100)

# main game loop
for round in range(1, rounds + 1):
    # generate random winning number
    win_number = random.randint(1, limit)
    # skip a line here
    print()

    print(f"Round {round}...")
    # ask user for first guess
    num_guess = get_valid_number(f"Guess the lucky number (between 1 and {limit}): ", limit)

    if win_number == num_guess:
        print("Awesome! You nailed it on the first try!")
        score += 5
    elif num_guess > win_number:
        print("That's not it. Guess lower this time.")
    else:
        print("That's not it. Guess higher this time.")

    # give the player a second chance if they didn't get the first guess
    if num_guess != win_number:
        num_guess = get_valid_number("Second chance: ", limit)

        if num_guess == win_number:
            score += 3
            print("You got it! Good job!")
        elif num_guess > win_number:
            print("That's still not it. Guess a bit lower.")
        else:
            print("That's still not it. Guess a bit higher.")

    # third and final chance
    if num_guess != win_number:
        num_guess = get_valid_number("Final guess: ", limit)

        if num_guess == win_number:
            score += 1
            print("Finally you got it right!")
        else:
            print(f"Wrong! The winning number was {win_number}.")

    print(f"Score: {score}")
    # skip line
    print()

accuracy = score / (5 * rounds) * 100
print(f"Great! After {rounds} rounds, your guessing accuracy is {accuracy:.1f}%")
