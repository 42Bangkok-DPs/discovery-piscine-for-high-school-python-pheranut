#!/usr/bin/env python3

user_input = input("Enter a number less than 25:  ")

try:
    # Convert input to a numeric variable
    number = int(user_input)

    # Check if the number is greater than 25
    if number > 25:
        print("Error")
    else:
        # Loop from the input number to 25
        for i in range(number, 26):
            print(f"Inside the loop, my variable is {i}")

except ValueError:
    print("Please enter a valid number.")
