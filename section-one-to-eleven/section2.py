# Tip Calculator
print("Welcome to the Tip Calculator")
bill_total = float(input("What was the total bill?\n$"))
num_of_people = int(input("How many people will be splitting the bill?\n"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15\n"))

per_person = round(bill_total * (percentage / 100) / num_of_people + (bill_total / num_of_people), 2)
print("Each person should pay: $", per_person)


# print("Haze"[2])
#
# two_digit_number = input()
#
# print(int(two_digit_number[0]) + int(two_digit_number[1]))

# print(3 * 3 + 3 / 3 - 3)
#
# print(3 / 3 * 3 - 3 + 3)
#
# # 1st input: enter height in meters e.g: 1.65
# height = input()
# # 2nd input: enter weight in kilograms e.g: 72
# weight = input()
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
# print(int(int(weight) / (float(height) ** 2)))

# print(round(2.666666, 2))

# name = "Haze"
# age = 32
# good = False
#
# print(f"You are {name}, aged {age} years, good in you? {good}.")
#
#
# age = input()
#
# weeks_left = (90 - int(age)) * 52
#
# print(f"You have {weeks_left} weeks left.")

# print(int(5) / int(2.7))