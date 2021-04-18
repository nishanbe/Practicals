"""Guitars Program"""
from prac_06.guitar import Guitar


def main():
    """This program will get and reflect the guitar information you enter"""
    name = input("Guitar: ")
    guitars = []
    while name != "":
        try:
            year = int(input("Year: "))
            if year > 2021:
                print("Year cannot be in the future")
                year = int(input("Year: "))

            cost = int(input("Cost: "))
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
            print("{guitar.name} ({guitar.year}), $ {guitar.cost:,.2f} added.".format(guitar=guitar))
            # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
            # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
            # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))
            # print(*guitars)
            name = input("Guitar: ")
        except ValueError:
            print("Invalid input, please try again.")
    else:
        name_width = max([len(guitar.name) for guitar in guitars])
        cost_width = max([len(str(guitar.cost)) for guitar in guitars])

        for i, guitar in enumerate(guitars, 1):
            # print("Guitar", i, ":", guitar.name, guitar.year)
            print(
                "Guitar {0}: {guitar.name:{1}} ({guitar.year:>4}), worth $ {guitar.cost:>{2},.2f}".format(i, name_width,
                                                                                                          cost_width,
                                                                                                          guitar=guitar))


if __name__ == '__main__':
    main()
