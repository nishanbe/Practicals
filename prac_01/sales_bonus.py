MENU = """This program to calculates and display your bonus based on your sales.   
"""
print(MENU)

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales <= 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    break
print("The bonus deserved is: ${:.2f}".format(bonus))
