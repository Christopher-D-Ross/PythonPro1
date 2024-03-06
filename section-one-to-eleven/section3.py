# 120cm

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height > 120:
#     print("You may board the roller coaster.")
#     age = int(input("How old are you?"))
#     if age > 18:
#         if input("Would you like a photo taken? yes or no ") == "yes":
#             print("Your ticket price is $15.")
#         else:
#             print("Your ticket price is $12.")
#     elif age >= 12 and age <= 18:
#         if input("Would you like a photo taken? yes or no ") == "yes":
#             print("Your ticket price is $10.")
#         else:
#             print("Your ticket price is $7.")
#     else:
#         if input("Would you like a photo taken? yes or no ") == "yes":
#             print("Your ticket price is $8.")
#         else:
#             print("Your ticket price is $5.")
# else:
#     print("Unfortunately you cannot ride this roller coaster.")

# number = input()
#
# if int(number) % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# year = int(input())
#
# if year % 4 == 0:
#     if year % 100 != 0:
#         print("Leap year")
#     elif year % 400 == 0:
#         print("Leap year")
#     else:
#         print("Not leap year")
# else:
#     print("Not leap year")


# Build an automatic pizza order program.
#
# Based on a user's order, work out their final bill.
#
# Small pizza (S): $15
#
# Medium pizza (M): $20
#
# Large pizza (L): $25
#
# Add pepperoni for small pizza (Y or N): +$2
#
# Add pepperoni for medium or large pizza (Y or N): +$3
#
# Add extra cheese for any size pizza (Y or N): +$1
#
# Example Input
# L
# Y
# N
# Example Output
# Thank you for choosing Python Pizza Deliveries!
# Your final bill is: $28.

# print("Welcome to Haze Pizza...")
# bill = 0
# size = input("What size pizza would you like? S, M, or L ")
# pepp = input("Would you like pepperoni? (Y or N): ")
# cheese = input("Would you like to add extra cheese? (Y or N): ")
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# if pepp == "Y" and size == "S":
#     bill += 2
# else:
#     bill += 3
# if cheese == "Y":
#     bill += 1
# print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")


# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# if add_pepperoni == "Y" and size == "S":
#     bill += 2
# elif add_pepperoni == "Y" and size != "S":
#     bill += 3
# if extra_cheese == "Y":
#     bill += 1
# print(f"Your final bill is: ${bill}.")

# LOVE CALCULATOR
# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.

# Then check for the number of times the letters in the word LOVE occurs.

# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is *z*."

print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?

lover_one = name1.lower()
lover_two = name2.lower()

true_count = 0
love_count = 0

true_count += lover_one.count("t")
true_count += lover_one.count("r")
true_count += lover_one.count("u")
true_count += lover_one.count("e")

true_count += lover_two.count("t")
true_count += lover_two.count("r")
true_count += lover_two.count("u")
true_count += lover_two.count("e")

love_count += lover_one.count("l")
love_count += lover_one.count("o")
love_count += lover_one.count("v")
love_count += lover_one.count("e")

love_count += lover_two.count("l")
love_count += lover_two.count("o")
love_count += lover_two.count("v")
love_count += lover_two.count("e")

score = str(true_count) + str(love_count)
score_int = int(score)


# For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:

"Your score is *z*."

if score_int < 10 or score_int > 90:
    print(f"Your score is {score_int}, you go together like coke and mentos.")
elif score_int > 40 and score_int < 50:
    print(f"Your score is {score_int}, you are alright together.")
else:
    print(f"Your score is {score_int}.")


print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

lover_one = name1.lower()
lover_two = name2.lower()

true_count = 0
love_count = 0

true_count += lover_one.count("t")
true_count += lover_one.count("r")
true_count += lover_one.count("u")
true_count += lover_one.count("e")

true_count += lover_two.count("t")
true_count += lover_two.count("r")
true_count += lover_two.count("u")
true_count += lover_two.count("e")

love_count += lover_one.count("l")
love_count += lover_one.count("o")
love_count += lover_one.count("v")
love_count += lover_one.count("e")

love_count += lover_two.count("l")
love_count += lover_two.count("o")
love_count += lover_two.count("v")
love_count += lover_two.count("e")

score = str(true_count) + str(love_count)
score_int = int(score)

if score_int < 10 or score_int > 90:
    print(f"Your score is {score_int}, you go together like coke and mentos.")
elif score_int > 40 and score_int < 50:
    print(f"Your score is {score_int}, you are alright together.")
else:
    print(f"Your score is {score_int}.")





