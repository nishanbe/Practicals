"""
CP1404/CP5632 Practical 05
Email Register
"""


def main():
    """This program allows you to store your email, predict and confirm your full name."""
    email = input("Email: ")
    predicted_full_name = extract_full_name(email)
    confirmed_name = input("Is your name {}? (Y/n) ".format(predicted_full_name)).upper()
    name = validate_name(predicted_full_name, confirmed_name)
    print(name)


def extract_full_name(email):
    """Extract the full name from the entered email"""
    extracted_name = email.split("@")[0]
    extracted_name = extracted_name.split(".")
    extracted_name = " ".join(extracted_name).title()
    return extracted_name


def validate_name(predicted_full_name, confirmed_name):
    """Validate predicted name and re-prompt if inaccurate"""
    if confirmed_name == "Y":
        name = predicted_full_name
    else:
        name = input("Name: ")
        name = name.title()
    return name


if __name__ == '__main__':
    main()
