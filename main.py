def encode(num_string):
    encoded_string = ""
    for i in num_string:
        temp = int(i) + 3
        if temp > 10:
            encoded_string += str(temp - 10)
        else:
            encoded_string += str(temp)
    return encoded_string


def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")


def main():
    while True:
        menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            print("")
        elif option == 2:
            print(f"The encoded password is {encode(password)}, and the original password is {password}.")
            print("")
        elif option == 3:
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()