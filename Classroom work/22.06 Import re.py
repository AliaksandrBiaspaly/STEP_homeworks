import re

some_text = "See your place See cowboy! See"

#x = input()  # ввод искомого текста
#match = re.findall((x), some_text.lower())
match1 = re.findall('\wee\w', some_text.lower())

print(match1)
print(len(match1))
print()
print(match1)
