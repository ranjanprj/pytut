import re

#The string property returns the search string:

txt = "The rain in 345345 Spain"
x = re.findall(r"\D+", txt)
s = '__'.join(x)
print(s)

