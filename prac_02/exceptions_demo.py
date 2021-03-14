try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
Questions & Answers

1.When will a ValueError occur?
When the user enters a character that is not an integer

2.When will a ZeroDivisionError occur?
When a user enters a 0 for either one of the questions. It occurs because dividing any number by 0 results in an error.  

3.Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes by using Try and except. You simply add a message after the except ZeroDivisionError:
"""