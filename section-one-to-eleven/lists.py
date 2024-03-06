names_of_grey = ["Somba", "Haze", "Icen", "Greysar"]

for name in names_of_grey:
    print(name)

print(f"Printing index 1 of names_of_grey: {names_of_grey[1]}")

names_of_grey.append("Maestarx")
new_name = names_of_grey[-1] = "Maestar"
print(f"Printing the index -1 in names_of_grey {new_name}")

vegetables = ["Spinach", "Kale", "Carrots"]
meats = ["Chicken", "Turkey", "Fish"]

# Nested Lists - A list that contains multiple lists
whole_meal = [vegetables, meats]

print(f"Printing whole_meal: {whole_meal}")

location = "A3"

print(location[0])

line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
location_letter = position[0]
location_number = int(position[1]) - 1
converted_letter = None
if location_letter == "A":
    converted_letter = 0
elif location_letter == "B":
    converted_letter = 1
else:
    converted_letter = 2

map[location_number][converted_letter] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")