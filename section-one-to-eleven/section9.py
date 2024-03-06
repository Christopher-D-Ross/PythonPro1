# Creating a dictionary with key, value pairs
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving an item or the value of a key from the dictionary.
print(programming_dictionary["Bug"])

# Adding items to the dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

# Creating an empty dictionary
empty_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."

# Looping through a dictionary
for key in programming_dictionary:
    print(key)  # This will print the key
    print(programming_dictionary[key])  # This will print the value

# Grading Program Exercise
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if 91 <= student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"

# Alternate Solution
for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
# 🚨 Don't change the code below 👇
print(student_grades)

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Little", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a List within a List
letters = ["A", "B", ["C", "D", "E"]]

# Nesting a Dictionary in a Dictionary
travel_log_revised = {
    "France": {
        "cities_visited": ["Paris", "Little", "Dijon"],
        "restaurants_visited": 10
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "restaurants_visited": 7
    }
}

# Nesting a Dictionary in a List
travel_log_list = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Little", "Dijon"],
        "restaurants_visited": 10
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "restaurants_visited": 7
     }
]

travel_log_list.append({"country": "Brazil", "cities_visited": ["Sao Paolo", "Rio De  Janeiro"], "restaurants_visited": 10})

print(travel_log_list)

country = input()  # Add country name
visits = int(input())  # Number of visits
list_of_cities = eval(input())  # create list from formatted string

travel_log_ex = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.
def add_new_country(place, num_of_visits, cities):
    travel_log_ex.append({"country": place,
                       "visits": num_of_visits,
                       "cities": cities})


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log_ex[2]['country']} {travel_log_ex[2]['visits']} times.")
print(f"My favourite city was {travel_log_ex[2]['cities'][0]}.")
