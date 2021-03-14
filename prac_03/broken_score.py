"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
# main should ask the user for their score and print the result.
# write a new function that takes in the user's score as a parameter and returns the result to be printed.
# The function should not print it.
import random


def main():
    score = float(input("Enter score: "))
    print(assess(score))
    print("-----------------")
    randomise_scores()


def assess(score):
    result = ""
    if score < 0:
        result = "Invalid score"
    else:
        if score > 100:
            result = "Invalid score"
        elif score >= 90:
            result = "Excellent"
        elif score >= 50:
            result = "Passable"
        elif score < 50:
            result = "Bad"

    return result


def randomise_scores():
    random_count = int(input("Enter the amount of random scores:"))
    print("Here are {:d} random scores:".format(random_count))
    for i in range(random_count):
        score = random.randint(1, 100)
        print("{} - The score {} is {}".format(i+1, score, assess(score)))


main()
