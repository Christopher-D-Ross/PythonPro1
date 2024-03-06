# Input a Python list of student heights
# Example: 151 145 179
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
sum_of_heights = 0
for height in student_heights:
    sum_of_heights += height

print(f"total height = {sum_of_heights}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {round(sum_of_heights / len(student_heights))}")