# https://www.youtube.com/watch?v=sa-TUpSx1JA

#text = "Достать ссылку на картинку <img src='bg.jpg'> в тексте </p>"
#<[a-z0-9.'=<> ]\w+\s[a-z0-9=]+[a-z0-9.'=<>]+
#<[a-z0-9.'=<> ]+>

import re

x = """text = "Достать ссылку на картинку <img src='bg.jpg'> в тексте </p>"""

print(*list(re.findall("<[a-z0-9.'=<> ]+>", x)))