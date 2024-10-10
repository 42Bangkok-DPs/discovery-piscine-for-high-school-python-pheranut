import math

def round_up(number):
    rounded_number = math.ceil(number)
    return rounded_number

try:
    num = input("Give me a number: ")
    number = float(num)
    result = round_up(number)
    print(result)
except ValueError:
    print("Error: Please enter a valid number.")