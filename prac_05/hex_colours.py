"""
CP1404/CP5632 Practical
Intermediate Exercises
"""

NAME_TO_COLOUR = {"red1": "#ff0000", "green1": "#00ff00", "blue1": "#0000ff",
                  "yellow1": "#ffff00", "cyan1": "#00ffff", "magenta": "#ff00ff",
                  "gray6": "#0f0f0f", "honeydew1": "#f0fff0", "white": "#ffffff",
                  "black": "#000000"}


def main():
    """This program allows you to get the hex code of colour names you enter"""
    print("Enter any of the colour names below to get its hex code:")
    print(*NAME_TO_COLOUR.keys(), sep=", ", end="\n\n")
    colour_name = input("Enter a colour name: ").lower()
    while colour_name != "":
        validate_name(colour_name)
        colour_name = input("Enter a colour name: ").lower()
    print("Thanks for using this program. Hold tight for the next version with more colours!")


def validate_name(colour_name):
    """Validate the colour name and respond"""
    if colour_name in NAME_TO_COLOUR:
        print(NAME_TO_COLOUR[colour_name], end="\n\n")
    else:
        print("\nInvalid name, please type one of the following colour names:")
        print(*NAME_TO_COLOUR.keys(), sep=", ", end="\n\n")


if __name__ == '__main__':
    main()
