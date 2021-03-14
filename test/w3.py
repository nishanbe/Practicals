number = int(input("Give me a number to square it:"))


def square_it(num):
    num = num * num
    return num


print("The square if", number, "is", square_it(number))
