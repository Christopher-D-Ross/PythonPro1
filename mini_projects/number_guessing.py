import random

# Number Guessing Game

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

the_number = random.randint(1, 100)


def guess_the_number(level):
    num_of_attempts = 0
    if difficulty == "easy":
        num_of_attempts += 10
    else:
        num_of_attempts += 5
    print(f"You have {num_of_attempts} attempts to guess the number.")
    while num_of_attempts > 0:
        guess = int(input("Make a guess: "))
        if guess > the_number:
            print("Too High.\nGuess again.")
            num_of_attempts -= 1
            print(f"You have {num_of_attempts} attempts left.")
        elif guess < the_number:
            print("Too Low.\nGuess again.")
            num_of_attempts -= 1
            print(f"You have {num_of_attempts} attempts left.")
        elif guess == the_number:
            print(f"Correct! The answer was {the_number}.")
            return
    print("You've run out of guesses, you lose.")


difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

guess_the_number(difficulty)
