"""
CP1404/CP5632 Practical 05
Email Register
"""


def main():
    """This program allows you to store multiple emails, predict and confirm names upon entry."""
    email_register = {}
    email = " "
    while email != "":
        try:
            email = input("Email: ")
            if email != "":
                validate_email(email)
                predicted_name = extract_full_name(email)
                accept_predicted = input("Is your name {}? (Y/n) ".format(predicted_name)).upper()
                name = validate_name(predicted_name, accept_predicted)
                # print("Stored name:", name)
                store_in_email_register(email_register, name, email)
                # print("Current register:", email_register)
                # email = input("Email: ")
                # validate_email(email)
            else:
                # print("You entered a blank email")
                # print(email_register)
                if email_register != "":
                    display_email_register(email_register)
        except ValueError:
            print("The email register is currently empty")


def validate_characters(email):
    """Validate characters in the entered email"""
    ending = email[-1]
    if "@" not in email:
        print("\tYour email must have the @ symbol")
        return False
    if "." not in email:
        print("\tYour email must have the (.) symbol")
        return False
    if ending == ".":
        print("\tYour email must not end with (.)")
        return False
    # print("Characters validated")
    return True


def count_dots(email):
    """Count the dots in the entered email"""
    dot_count = 0
    for char in email:
        if char == ".":
            dot_count += 1
    return dot_count


def validate_corporate_formatting(email):
    """Validate the entered email if it follows the format firstname.lastname@company.com"""
    bypass = False
    dot_count = count_dots(email)
    valid_formatting = True
    while not bypass and dot_count == 1 and valid_formatting:
        print("Your email does not comply with the corporate standard formatting\n"
              "\tExample: firstname.lastname@company.com\n")
        proceed = input('Would you like to proceed with "{}"? (Y/n) '.format(email)).upper()
        if proceed in ("Y", ""):
            valid_formatting = True
            bypass = True
            # print("---Yes taken as a response")

        else:
            valid_formatting = False
            bypass = True
            # print("Invalid formatting choice")
    # print("--Format validation result:", valid_formatting)
    return valid_formatting


def validate_email(email):
    """Validate the entered email for characters and formats"""
    valid_email = False
    while not valid_email:
        valid_characters = validate_characters(email)
        if not valid_characters:
            valid_email = False
            email = input("Email: ")
        else:
            # print("---Char seems ok")
            valid_formatting = validate_corporate_formatting(email)
            if not valid_formatting:
                # print("---Format invalid")
                valid_email = False
                email = input("Email: ")
            else:
                # print("---Passed character & formatting validation")
                valid_email = True
    # print("--Validated email is:", email)
    return email


def extract_full_name(email):
    """Extract the full name from the entered email"""
    extracted_name = email.split("@")[0]
    extracted_name = extracted_name.split(".")
    extracted_name = " ".join(extracted_name).title()
    return extracted_name


def validate_name(predicted_name, accept_predicted):
    """Validate predicted name and re-prompt if inaccurate"""
    if accept_predicted in ("Y", ""):
        # print("accept_predicted is", accept_predicted)
        name = predicted_name
    else:
        name = input("Name: ")
        if name == "":
            print("Invalid. Name can not be black")
            name = input("Name: ")
        name = name.title()
    return name


def store_in_email_register(email_register, name, email):
    """Store the name and email in an email registry (dictionary)"""
    email_register[name] = email


def display_email_register(email_register):
    """Display the email register in a nicely formatted manner"""
    calculated_width = count_width_of_longest_name(email_register)
    for name, email in email_register.items():
        print("{:{}} ({})".format(name, calculated_width, email))


def count_width_of_longest_name(email_register):
    """Count the the width of the longest name to use it for formatting"""
    list_of_names = list(email_register.keys())
    name_lengths = []
    for name in list_of_names:
        name_lengths.append(len(name))
    longest_name_width = max(name_lengths)
    return longest_name_width


if __name__ == '__main__':
    main()
