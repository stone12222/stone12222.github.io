s='url1 <a href="http://google.com">google</a> url2 <a href="http://apple.com">apple</a>'

import re
m=re.finditer('<a (href)="(.+?)">',s)

for e in m:
    print(e.group()) # full match
    print(e.group(0))
    print(e.group(1)) # return group
    print(e.group(2)) # return group
