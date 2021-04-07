"""
CP1404/CP5632 Practical
Count Word Occurrences
"""


def main():
    """This program counts the occurrences of each word in any sentence you enter"""

    print("Type a sentence to get the count of each word.")
    # Get text from the user
    text = input("Text: ")

    # Create a sorted list of words from the test
    words = text.split()
    words.sort()


if __name__ == '__main__':
    main()
