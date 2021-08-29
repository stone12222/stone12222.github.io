s='url1 <a href="http://google.com">google</a> url2 <a href="http://apple.com">apple</a>'
import re

#
# lazy quantifier
matches=re.findall('<a href="http://.+?">',s)
print(matches)

# capturing group
matches=re.findall('<a href="(http://.+?)">',s)
print(matches)

#
matches=re.finditer('<a href="(http://.+?)">',s)
for e in matches:
    # print(e.group())
    # full match, group
    print(e.group(0))# return full match
    print(e.group(1))# return group