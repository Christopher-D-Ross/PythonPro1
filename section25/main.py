
import csv
import pandas

# with open("weather_data.csv") as file:
#     data = file.readlines()
#     for line in data:
#         print(line.strip())

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         print(row)


# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#         else:
#             temperatures.append(row[1])
#     print(temperatures)

csv_data = pandas.read_csv("weather_data.csv")
print(csv_data)
print(csv_data["temp"])

data_dictionary = csv_data.to_dict()
print(data_dictionary)

temp_list = csv_data["temp"].to_list()

print(sum(temp_list) / len(temp_list))

print(csv_data["temp"].mean())
print(csv_data["temp"].max())

# Get Data in Columns
print(csv_data["condition"])
print(csv_data.condition)

# Get Data in Rows
print(csv_data[csv_data.day == "Monday"])

# Get the row of data that had the max temperature.
print(csv_data[csv_data.temp == csv_data.temp.max()])

monday = csv_data[csv_data.day == "Monday"]
print((monday.temp[0] * 1.8) + 32)

# Create a DataFrame from scratch
student_data = {
    "students": ["Somba", "Kalen", "Icen"],
    "id-numbers": [267, 222, 136]
}
data = pandas.DataFrame(student_data)
print(data)

# Creating a .csv file using a DataFrame
data.to_csv("new-data.csv")
