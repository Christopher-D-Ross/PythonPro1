import random
import section7_hangman_extras

print(section7_hangman_extras.logo)

lives = 6

chosen_word = section7_hangman_extras.word_list[random.randint(0, len(section7_hangman_extras.word_list))]

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display.append("_")

wrong_letters = []

# ALTERNATIVE while condition:
# while "_" not in display:
while display.__contains__("_"):
    guess = input("\nGuess a letter: ").lower()

    for index in range(0, len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess
    if guess not in chosen_word and guess not in wrong_letters:
        lives -= 1
        wrong_letters.append(guess)
        print(f"The letter '{guess}' is not in this word. TRY AGAIN!!!!!!")
        print("Wrong Letters", wrong_letters)
    elif guess in wrong_letters:
        print(f"You already tried the letter '{guess}' smart person, try another letter.")
    print(section7_hangman_extras.stages[lives])
    print(display)
    if lives == 0:
        print("You Lose...")
        break
    if "_" not in display:
        print("\nYou Win!!")

