import random
import section4

guess = random.randint(0, 666)

print("Printing the value of pi: ", section4.pi, "from the section4.py module.")
print(section4.mak_pro)
print(f"The D Reaper rando Number => {guess}")


random_float = random.random()
print(random_float)

random_whole_plus_decimal = random.random() * 5
print(f"Printing random_whole_plus_decimal => {random_whole_plus_decimal}")

coin_toss = random.randint(0, 1)

if coin_toss == 0:
  print("Tails")
else:
  print("Heads")