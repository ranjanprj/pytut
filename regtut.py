import re

#The string property returns the search string:

txt = "The rain in 345345 Spain"
# \d to include digits, \D to exclude digits
x = re.findall(r"\D+", txt)
s = '__'.join(x)
print(s)

