import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# phonetic_csv is considered a Dataframe
phonetic_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dictionary = {row.letter: row.code for (index, row) in phonetic_csv.iterrows()}
print(phonetic_dictionary)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()
phonetic_list = [phonetic_dictionary[letter] for letter in user_word]
print(phonetic_list)
