from prac_06.guitar import Guitar

guitar = "Gibson L-5 CES"
guitar_year = 1922
guitar_cost = 99

another = "Another Guitar"
another_year = 2013
another_cost = 129

g1 = Guitar(guitar, guitar_year, guitar_cost)
g2 = Guitar(another, another_year, another_cost)

print(g1.name, "get_age() - Expected 99. Got", g1.get_age())
print(g2.name, "get_age() - Expected 99. Got", g2.get_age())
print(g1.name, "is_vintage() - Expected True. Got", g1.is_vintage())
print(g2.name, "is_vintage() - Expected False. Got", g2.is_vintage())
