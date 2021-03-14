"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")

    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):

        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    password_too_short = False
    password_too_long = False
    if len(password) < MIN_LENGTH:
        password_too_short = True
    if len(password) > MAX_LENGTH:
        password_too_long = True

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
        if char.isdigit():
            count_digit += 1
        if char.isupper():
            count_upper += 1
        if char.islower():
            count_lower += 1
    if SPECIAL_CHARS_REQUIRED:
        for i in password:
            special = SPECIAL_CHARACTERS.find(i)
            if special >= 0:
                count_special += 1
    else:
        # To avoid detection error of a special character (keep count over 0)
        count_special += 1

    """
    # Testing the detection of each specification
    print("count_digit = ", count_digit)
    print("count_upper = ", count_upper)
    print("count_lower = ", count_lower)
    print("count_special = ", count_special)
    """
    # TODO: if any of the 'normal' counts are zero, return False
    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero
    if count_lower < 1 or count_upper < 1 or count_digit < 1 or count_special < 1:
        if password_too_long:
            print("Your password can not be longer than", MAX_LENGTH, "characters long")
        elif password_too_short:
            print("Your password must be more that", MIN_LENGTH, "characters long")
        else:
            print("Invalid password. Your chosen password does not include:")
            if count_digit == 0:
                print("\tA number")
            if count_lower == 0:
                print("\tA lowercase character")
            if count_upper == 0:
                print("\tAn upper character")
            if SPECIAL_CHARS_REQUIRED:
                if count_special == 0:
                    print("\tA special character:", SPECIAL_CHARACTERS)

            print("Please try again:")
        return False
    # if we get here (without returning False), then the password must be valid
    return True


main()
