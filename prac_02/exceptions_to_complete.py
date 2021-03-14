finished = False
result = 0

print("\nLet's prove that any number multiplied by zero equals zero")
while not finished:
    try:
        num = int(input("Enter a number: "))
        result = num * 0
        print("You've entered", num)
        print(num, " x 0 = ", result)
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("The result is:", result)
