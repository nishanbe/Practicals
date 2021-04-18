class ProgrammingLanguage:
    def __init__(self, typing, reflection, year):
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        return False


typing = input("Type: ")
reflection = "Yes"
year = 1991

p1 = ProgrammingLanguage(typing, reflection, year)
print(p1.is_dynamic())
