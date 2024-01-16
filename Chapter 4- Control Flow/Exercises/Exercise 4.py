age = int(input("Please input the age: "))

if age < 2:
    print("This person is a baby.")
elif 2 <= age < 4:
    print("This person is a toddler.")
elif 4 <= age < 13:
    print("This person is a kid.")
elif 13 <= age < 20:
    print("This person is a teenager.")
elif 20 <= age < 65:
    print("This person is an adult.")
else:
    print("This person is an elder.")