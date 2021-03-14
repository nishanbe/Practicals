MIN_LENGTH = 4
# write a program that asks the user for a password
password = input("Enter a password: ")

# with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
while len(password) < MIN_LENGTH:
    print("The password you entered is too short, enter at least", MIN_LENGTH, "characters.")
    password = input("Enter a password: ")
else:
    # The program should then print asterisks as long as the word
    for char in password:
        print("*", end="")
