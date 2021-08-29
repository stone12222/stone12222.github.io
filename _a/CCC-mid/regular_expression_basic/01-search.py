import re

s="655 wiNdermere rd. London ON"

# return Match object
# rex=re.compile('nd')
# match=rex.search(s)

match=re.search('nd', s, re.I)
print(match)

if match!=None:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
else:
    print('not found')

# re.I : ignore case
# re.M : Makes $ match the end of a line
# (not just the end of the string) and makes ^
# match the start of any line
# (not just the start of the string).
