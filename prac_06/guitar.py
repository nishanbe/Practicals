class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : {} ".format(self.name, self.year, self.cost)

    def __repr__(self):
        return "{} ({}) : {} ".format(self.name, self.year, self.cost)

    def get_age(self):
        age = 2021 - self.year
        return age

    def is_vintage(self):
        age = self.get_age()
        if age >= 50:
            return True
        return False

# Testing
# n = "Yamaha"
# y = 1922
# c = 292
#
# g1 = Guitar(n, y, c)
# print(g1)
# print(g1.get_age())
# print(g1.is_vintage())
