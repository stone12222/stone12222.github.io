s = 'aa aa11 11aa aa'

'''
capturing but not return as match
or
return zero-length match

(?=pattern)     look ahead positive
(?!pattern)     look ahead negative
(?<=pattern)     look behind positive
(?<!pattern)     look behind negative
'''


import re
result = re.finditer('(aa)\d+',s)

for e in result:
    print(e.span())
    print(e.group())

#look behind positive
result = re.finditer('(?<=\d)aa',s)
for e in result:
    print(e.span())
    print(e.group())

#look behind negative
print('######')
result = re.finditer('(?<=!\d)aa',s)
for e in result:
    print(e.span())
    print(e.group())