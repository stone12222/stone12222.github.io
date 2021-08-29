s="655 wiNdermere rd. London ON"

#
pos=s.find('nd')
print(pos)
pos=s.find('Nd')
print(pos)

# new
import re
result=re.search('nd',s,re.I)
print(result.span())
print(result.start())

# search all
result=re.findall('nd',s,re.I)
print(result)

# search all
result=re.finditer('nd',s,re.I)
for r in result:
    print(r.group(),'at',r.span())

