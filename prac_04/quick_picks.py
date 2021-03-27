"""
CP1404/CP5632 Practical
"Quick Pick" Lottery Ticket Generator
"""
import random

NUMBERS_PICK_SET = 6
MIN_RANGE = 1
MAX_RANGE = 45


def main():
    user_count = int(input("How many quick picks? "))
    picks = []
    for pick in range(NUMBERS_PICK_SET):
        picks.append(0)

    for count in range(user_count):
        almost_random_picks = [random.randint(MIN_RANGE, MAX_RANGE) for pick in picks]

        for pick in almost_random_picks:
            while pick in almost_random_picks:
                pick = random.randint(1, 45)
                # print("Repetition Detected")
        # print(str(almost_random_picks))
        almost_random_picks.sort()
        random_picks = almost_random_picks
        # print("{:2} {:2} {:2} {:2} {:2} {:2}".format(*random_picks))
        # print(" ".join("{:2}".format(pick) for pick in random_picks))
        # Alternative of the previous line as a loop
        for number in random_picks:
            print("{:2}".format(number), end=" ")
        print("")


'''
            quickset = quick_pick for quick_pick in quick_pick

                #print(len(number), end=" ")
                if len(number) > 1:
                    print("Repetition Detected")
            print("{:2}".format(quick_pick), end=" ")
        print(" one")
        print("quick_pick is:", quick_pick)
'''

main()
