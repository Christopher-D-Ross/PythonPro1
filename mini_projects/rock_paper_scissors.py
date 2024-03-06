import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps_choice = input("Type 0 for 'Rock', 1 for 'Paper', or 2 for 'Scissors'. The computer's choice will be revealed after your decision is made.\n")

rps_list = [rock, paper, scissors]
rps_list_names = ["Rock", "Paper", "Scissors"]

print(rps_list[int(rps_choice)] + "\n")

print("The Computer chose:\n")
computer_rps_choice = random.randint(0, 2)
print(rps_list[computer_rps_choice])

if rps_choice == "0" and str(computer_rps_choice) == "2":
    print(f"You win. {rps_list_names[int(rps_choice)]} beats {rps_list_names[computer_rps_choice]}.")
elif rps_choice == "2" and str(computer_rps_choice) == "1":
    print(f"You win. {rps_list_names[int(rps_choice)]} beats {rps_list_names[computer_rps_choice]}.")
elif rps_choice == "1" and str(computer_rps_choice) == "0":
    print(f"You win. {rps_list_names[int(rps_choice)]} beats {rps_list_names[computer_rps_choice]}.")
elif int(rps_choice) == computer_rps_choice:
    print("It's a draw.")
else:
    print(f"You lose. {rps_list_names[computer_rps_choice]} beats {rps_list_names[int(rps_choice)]}.")