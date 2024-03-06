import random
import os

import higher_lower_art
import higher_lower_data

# An array of Dictionaries is how the data is stored.
# [
#   {
#       'name': 'Instagram',
#       'follower_count': 346,
#       'description': 'Social media platform',
#       'country': 'United States'
#   }
# ]
people = higher_lower_data.data


def person_string(number):
    person = people[number]["name"]
    desc = people[number]["description"]
    origin = people[number]["country"]
    return f"{person}, a {desc}, from {origin}."


def follower_count(number):
    followers = people[number]["follower_count"]
    return followers


def get_random_num():
    return random.randint(0, len(people) - 1)


def save_winner(num_one, num_two):
    if follower_count(num_one) > follower_count(num_two):
        return "A"
    else:
        return "B"


def play_higher_lower():
    guess_right = True
    comp_a = get_random_num()
    comp_b = get_random_num()
    current_score = 0
    while guess_right:

        while comp_a == comp_b:
            comp_b = get_random_num()

        person_a = person_string(comp_a)

        person_b = person_string(comp_b)

        print(higher_lower_art.logo)
        if current_score > 0:
            print(f"You're right! Current score: {current_score}")
        print(f"Compare A: {person_a}")
        print(higher_lower_art.vs)
        print(f"Against B: {person_b}")

        attempt = input("Who has more followers? Type 'A' or 'B': ").upper()
        if attempt == save_winner(comp_a, comp_b):
            current_score += 1
            os.system("clear")
            comp_a = comp_b
            comp_b = get_random_num()
        else:
            os.system("clear")
            guess_right = False
            print(higher_lower_art.logo)
            print(f"Sorry that's wrong. Final score: {current_score}")


play_higher_lower()
