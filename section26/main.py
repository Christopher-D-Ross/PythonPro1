import random

import pandas

first_names = ["Somba", "Greysar", "Maestar", "Nahci", "Snuuz", "Spirah", "Icen", "Pharen", "Senza", "Nova", "Shadow",
               "Remor"]

full_names = [f"{name} Kalen" for name in first_names]
print(full_names)

double_up = [num + num for num in range(1, 5)]
print(double_up)

six_letters = [name for name in first_names if len(name) == 6]
print(six_letters)

with open("file1.txt") as file_one:
    file_one_nums = file_one.readlines()
    strip_one = [int(num.strip()) for num in file_one_nums]

with open("file2.txt") as file_two:
    file_two_nums = file_two.readlines()
    strip_two = [int(num.strip()) for num in file_two_nums]

result = [num for num in strip_one if num in strip_two]

print(result)

name_and_score = {key: random.randint(1, 100) for key in full_names}
print(name_and_score)
passed_scores = {key: value for (key, value) in name_and_score.items() if value > 60}
print(passed_scores)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_list = sentence.split(" ")
letter_count = {key: len(key) for key in word_list}

print(letter_count)

weather_celsius = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_fahrenheit = {key: (value * 9/5) + 32 for (key, value) in weather_celsius.items()}
print(weather_fahrenheit)


personnel_data = {
    "students": ["Somba", "Kalen", "Icen"],
    "id-numbers": [267, 222, 136]
}
personnel_dataframe = pandas.DataFrame(personnel_data)
print(personnel_dataframe)
for (index, row) in personnel_dataframe.iterrows():
    print(index)
    print(row.students)
