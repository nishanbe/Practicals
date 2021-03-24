"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_nicely(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME, "r")
    all_parts = []
    for line in input_file:
        # print("This is a line", line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip("\n")  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        all_parts.append(parts)

    input_file.close()
    return all_parts


def display_nicely(all_parts):
    for part in all_parts:
        print(part[0], "is taught by", part[1], "and has", part[2], "students")
# CP1401 is taught by Ada Lovelace and has 192 students


main()
