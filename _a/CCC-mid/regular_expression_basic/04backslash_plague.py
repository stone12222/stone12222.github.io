# surround word with |

import re
s='333 SUNNY Broad road'
s1=re.sub('\b','|',s)
print(s1)

# problem: backslash_plague
# \b has special meaning (backspace) for python string
print('abc\b')

# we need escape \
s1=re.sub('\\b','|',s)
print(s1)

# or use raw string which tell python nothing in this string is special (means no escape codes)
s1=re.sub(r'\b','|',s)
print(s1)
