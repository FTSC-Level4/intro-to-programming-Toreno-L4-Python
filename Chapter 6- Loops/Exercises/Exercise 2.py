loop = "true"

while loop == "true":
    age = int(input("Welcome to the Cinema! Please input your age for your ticket price: "))
    if age < 3:
        print("Your ticket is [FREE], thank you. Please come again.\n")
    elif 3 <= age <= 12:
        print("Your ticket price is [10$], thank you. Please come again.\n")
    else:
        print("Your ticket price is [15$], thank you. Please come again.\n")