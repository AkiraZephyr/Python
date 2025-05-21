import os
# Writing to a file
with open("output.txt", "w") as file:
    message = "Hello, world!\n"
    file.write(message)
# Reading from a file
with open("output.txt", "r") as file:
    data = file.read()
    print("Data read from file:", data)
# Removing the file
os.remove("output.txt")
