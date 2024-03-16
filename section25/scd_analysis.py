import pandas

csv_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240314.csv")

squirrel_data = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [csv_data["Primary Fur Color"].to_list().count("Gray"),
              csv_data["Primary Fur Color"].to_list().count("Cinnamon"),
              csv_data["Primary Fur Color"].to_list().count("Black")]
}

squirrel_data_frame = pandas.DataFrame(squirrel_data)

print(squirrel_data_frame.to_csv())
