target = int(input())  # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

even_number_sum = 0
for number in range(0, target + 1):
    if number % 2 == 0:
        even_number_sum += number

print(even_number_sum)

# Alternate Solution

