"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TO DO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                "WA": "Western Australia", "ACT": "Australian Capital Territory",
                "VIC": "Victoria", "TAS": "Tasmania"}
MENU = """Type the state code to reveal its name
To list all codes and names press enter anytime."""
# print(CODE_TO_NAME)
print(MENU)
state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
print("Here is a list of all state codes and name for your reference:")

for code, name in CODE_TO_NAME.items():
    print("{:3} is {}".format(code, name))
