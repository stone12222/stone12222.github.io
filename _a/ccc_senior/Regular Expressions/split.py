
s = 'abc | bcd | efg'

#no re

words = [e.strip() for e in s.split(' | ')]
print(words)

#re
import re
words = re.split('\ss*\|\s*',s)
print(words)