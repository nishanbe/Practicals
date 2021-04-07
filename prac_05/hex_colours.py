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
    print(*NAME_TO_COLOUR.keys(), sep=", ")
    colour_name = input("Enter a colour name: ").upper()
    while colour_name != "":
        colour_name = input("Enter a colour name: ").upper()

    print("Thanks for using this program. Hold tight for the next version!")


if __name__ == '__main__':
    main()
