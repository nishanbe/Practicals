from prac_06.programming_language import ProgrammingLanguage


ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)


# typing = input("Type: ")
# reflection = "Yes"
# year = 1991
#
# p1 = ProgrammingLanguage(typing, reflection, year)
# print(p1.is_dynamic())
print(ruby)
print(python)
print(visual_basic)
print("------------------------------------")

languages = [ruby, python, visual_basic]

print("The dynamically typed languages are:")
dynamic_languages = [lang.name for lang in languages if lang.is_dynamic()]

print(*dynamic_languages, sep="\n")
#
# for lang in languages:
#     print(lang)