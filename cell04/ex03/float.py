 #!/usr/bin/env python3
def czech(number):
    if number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")

try:
    num = input("Give me a number: ")
    number = float(num)
    czech(number)
except ValueError:
    print("Error: Please enter a valid number.")
