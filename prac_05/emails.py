"""
CP1404/CP5632 Practical 05
Email Register
"""


def main():
    """This program allows you to store your email, predict and confirm your full name."""
    email = input("Email: ")
    print(extract_full_name(email))


def extract_full_name(email):
    """Extract the full name from the entered email"""
    extracted_name = email.split("@")[0]
    extracted_name = extracted_name.split(".")
    extracted_name = " ".join(extracted_name).title()
    return extracted_name


if __name__ == '__main__':
    main()
