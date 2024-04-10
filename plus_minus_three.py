def menu():
    encoded = ""
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
            encoded = coding(option, encoded)
        elif option == 2:
            coding(option, encoded)
        else:
            break

def coding(option, encoded):
    if option == 1:
        password = input("Please enter your password to encode: ")
        encoded = ""
        for char in password:
            encoded += chr(ord(char) + 3)
        print("Your password has been encoded and stored!")
        return encoded
    elif option == 2:
        decoded = ""
        for char in encoded:
            decoded += chr(ord(char) - 3)
        print(f"The encoded password is {encoded}, and the decoded password is {decoded}")

if __name__ == "__main__":
    menu()
