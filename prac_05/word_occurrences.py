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

    # Create a dictionary out from the list with each word and its count
    words_dict = {}
    for word in words:
        words_dict[word] = words_dict.get(word, 0) + 1

    # Find the width of the longest word
    word_lengths = []
    for word in words:
        word_lengths.append(len(word))
    longest_word_width = max(word_lengths)


if __name__ == '__main__':
    main()
