MIN_PASSWORD_LENGTH = 4


def main():
    password = get_password(MIN_PASSWORD_LENGTH)
    print_asterisk_per_character(password)


def get_password(min_length):
    # write a program that asks the user for a password
    password = input("Enter a password: ")
    # with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
    while len(password) < min_length:
        print("The password you entered is too short, enter at least", min_length, "characters.")
        password = input("Enter a password: ")
    return password


def print_asterisk_per_character(count):
    for char in count:
        print("*", end="")


main()
