# This is Nicholas Murillo's code

def encode(num_string):  # encoding an inputted string
    encoded_string = ""  # starts empty string
    for i in num_string:
        temp = int(i) + 3  # for every number in string, add 3
        if temp >= 10:  # if number surpasses 10, subtract 10 to be within 0-9
            encoded_string += str(temp - 10)  # add to encoded string
        else:
            encoded_string += str(temp)  # add to encoded string
    return encoded_string


# This method decodes an already encoded password by subtracting 3 from each number
def decode(stringy):
    decoded_string = ""
    for i in stringy:
        if int(i) < 3:  # If the number is less than 3, start back at 9 instead of going into negative values
            dif = abs(int(i) - 3)
            decoded_string += str(10 - dif)
        else:
            decoded_string += str(int(i)-3)  # Subtract 3 from each number
    return decoded_string


def menu():  # menu printed every time in the loop
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")


def main():
    while True:
        menu()
        option = int(input("Please enter an option: "))  # option given by user
        if option == 1:  # if option is 1, encode input
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            print("")
        elif option == 2:  # if option is 2, display encoded and original password
            encoded = encode(password)
            print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}.")
            print("")
        elif option == 3:  # if option is 3, stop loop
            break
        else:  # if option is invalid, continue loop
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
