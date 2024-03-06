from caesar_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(code_type, word, word_shift):
    shifted_text = ""
    if code_type == "encode" and word_shift > len(alphabet):
        word_shift = word_shift % 26

    for letter in word:
        if code_type == "encode":
            if letter.isnumeric() or letter == " " or not letter.isalpha():
                shifted_text += letter
            elif alphabet.index(letter) + shift > len(alphabet) - 1:
                shifted_text += alphabet[alphabet.index(letter) + word_shift - 26]
            else:
                shifted_text += alphabet[alphabet.index(letter) + word_shift]
        elif code_type == "decode":
            if letter.isnumeric() or letter == " " or not letter.isalpha():
                shifted_text += letter
            elif alphabet.index(letter) - shift < 0:
                shifted_text += alphabet[alphabet.index(letter) - word_shift + 26]
            else:
                shifted_text += alphabet[alphabet.index(letter) - word_shift]
    print(f"The {direction}d text is {shifted_text}")


yes_or_no = ""
while yes_or_no != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    yes_or_no = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
