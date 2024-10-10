def swap_case(s):
    return s.swapcase()

if __name__ == "__main__":
    user_input = input("Please enter a string: ")
    result = swap_case(user_input)
    print(result)