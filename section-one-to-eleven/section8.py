# def greet():
#     print("Somba")
#     print("Kalen")
#     print("Haze")
#
#
# greet()
#
#
# def greet_person(name, location):
#     print(f"Blue Grey Day in {location} {name}")
#
#
# greet_person("Icen", "Hell")
#
#
# def another_way_to_input_parameters(a, b, c):
#     print(a + b + c)
#
#
# another_way_to_input_parameters(c=10, a=2, b=6)



# Write your code below this line 👇
import math

# def paint_calc(height, width, cover):
#   cans = math.ceil((height * width) / cover)
#   print(f"You'll need {cans} cans of paint.")
#
#
# # Write your code above this line 👆
# # Define a function called paint_calc() so the code below works.
#
# # 🚨 Don't change the code below 👇
# test_h = int(input()) # Height of wall (m)
# test_w = int(input()) # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


# Write your code below this line 👇

# def prime_checker(number):
#     is_more_div = False
#     for num in range(1, number + 1):
#         if number % num == 0:
#             if num != 1 and num != number:
#                 is_more_div = True
#     if is_more_div == True:
#         print("It's not a prime number.")
#     else:
#         print("It's a prime number.")
#
#
# # Write your code above this line 👆
#
# # Do NOT change any of the code below👇
# n = int(input())  # Check this number
# prime_checker(number=n)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# print(len(alphabet))

over_cipher = 45 % 26

over_over_cipher = 1000 % 26

reverse_over_over_cipher = 26 % 90

print(f"over_cipher = {over_cipher}")

print(f"over_over_cipher = {over_over_cipher}")

print(f"reverse_over_over_cipher = {reverse_over_over_cipher}")

a45 = "t"