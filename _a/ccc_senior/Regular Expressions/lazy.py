s = 'url1 <a href="http://google.com">google</a> url2 <a href="http://apple.com">apple</a>'
import re
#
matches = re.findall('<a href = "http://.+?',s)
print(matches)

#capturing group
#full match, group
matches = re.findall('<a href = "http://.+?',s)
print(matches)

#
matches = re.findall('<a href = "http://.+?',s)
for e in matches:
    print(e.group(0))
    print(e.group(1))