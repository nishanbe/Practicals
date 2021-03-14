"""
Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92
"""
total = 0
items = int(input("Number of items: "))
for i in range(items):
    price = int(input("Price of item: "))
    total = price + total
if total > 100:
    total = total - (total * 0.10)
print("Total price for", items, "items is ${:.2f}".format(total))

