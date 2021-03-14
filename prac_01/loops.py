print("All of the odd numbers between 1 and 20 with a space between each one")
for i in range(1, 21, 2):
    print(i, end=' ')


print("\n\nCount in 10s from 0 to 100")
for i in range(0, 101, 10):
    print(i, end=' ')

print("\n\ncount down from 20 to 1")
for i in reversed(range(1, 21, 1)):
      print(i, end=' ')

stars = int(input("\n\nHow many stars would you like to see? Enter a number: "))

for i in range(stars):
    print("*", end="")


stars = int(input("\n\nPattern will be created! Enter a number: "))
for i in range(stars):
    for x in range(0, i+1):
        print("*", end="")
    print("")