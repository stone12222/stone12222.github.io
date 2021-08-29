s='123 SUNNY BROAD RoAD'


# 123 SUNNY BROAD RD

# limit: case sensitive, not accurate for search
# s=s.replace('ROAD','RD')
# print(s)

# backslash plague
import re
# result=re.sub('\sROAD',' RD',s)
result=re.sub(r'\bROAD','RD',s,flags=re.IGNORECASE)
print(result)


'''
python r'\bROAD'

re engine \bROAD
'''




