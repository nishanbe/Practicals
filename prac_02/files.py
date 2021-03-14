
name = input("Enter your name: ")
in_file = open("name.txt", "w")
in_file.write(name)
in_file = open("name.txt", "r")
print("Your name is", in_file.read())
in_file.close()


the_file = open("numbers.txt", "r")
number1 = int(the_file.readline())
number2 = int(the_file.readline())
result = number1 + number2
print("The result of adding the first 2 numbers \nfrom the file 'numbers.txt' is:", result)
