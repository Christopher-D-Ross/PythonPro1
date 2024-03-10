with open("../../../Desktop/info-text.txt") as readFile:
    contents = readFile.read()
    print(contents)

# mode="w" for writing
with open("info-text.txt", mode="w") as writeFile:
    writeFile.write("Haze and Rain")

# # mode="a" for appending
with open("info-text.txt", mode="a") as writeFile:
    writeFile.write(" makes for Grey days.")

# Writing to a file that doesn't exist will create that file.
with open("kalen-file.txt", mode="w") as writeFile:
    writeFile.write("Somba Kalen")


# file = open("info-text.txt")
# contents = file.read()
# print(contents)
# file.close()
