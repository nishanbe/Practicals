"""
try:
    suite
except ErrorType
    suite

try:
    name = int(input("Name: "))
except ValueError:
    print("what the hell man?")
"""
valid_age = False
while not valid_age:
    try:
        age = input("Age: ")

        if age.isalpha():
            print("Please type a number not a character")
        elif int(age) < 0:
            print("Your age can not be negative")
        else:
            print("Thank you!")
            valid_age = True
    except ValueError:
        print('You entered "{}", that is invalid'.format(age))
    except NameError:
        print("Invalid age")
print("Your {} years old man!".format(age))
