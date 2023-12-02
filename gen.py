import random


def get_input():
    while True:
        try:
            quantity = int(input("How many passwords do you want to generate? "))
            break
        except ValueError:
            print("\nPlease enter a number!")
            continue
    while True:
        try:
            length = int(input("How long do you want your password to be? "))
            break
        except ValueError:
            print("\nPlease enter a number!")
            continue
    while True:
        special_chars = input(
            "Do you want to include special characters? (y/n) "
        ).lower()
        if special_chars == "y" or special_chars == "n":
            break
        else:
            print("\nPlease enter either 'y' or 'n'!")
            continue
    return quantity, length, special_chars


def get_character_set(special_chars):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    special_charset = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    if special_chars == "y":
        return chars + special_charset
    else:
        return chars


def generate_password(qty, length, characters):
    passwords = []
    for x in range(qty):
        password = ""
        for i in range(length):
            password += random.choice(characters)
        passwords.append(password)
    return passwords


def pp_password(password):
    print("\n")
    for i, password in enumerate(passwords):
        print(str(i + 1) + ".", password)


while True:
    print("\nWelcome to the password generator!\n")
    quantity, length, special_chars = get_input()
    char_set = get_character_set(special_chars)
    passwords = generate_password(quantity, length, char_set)
    pp_password(passwords)
    while True:
        user_input = input("\nWould you like to continue? (y/n) ").lower()
        if user_input == "y" or user_input == "n":
            break
        else:
            print("\nPlease enter either 'y' or 'n'!")
            continue
    if user_input == "n":
        break
