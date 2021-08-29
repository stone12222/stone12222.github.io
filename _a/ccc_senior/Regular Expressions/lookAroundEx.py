# select protocols
text= """
http://www.forta.com/
https://mail.forta.com/
ftp://ftp.forta.com/
"""

# look ahead
import re
protocols=re.finditer('\w+(?=:)',text)
for p in protocols:
   print(p.group()) # full match

# look behind
servers=re.finditer('(?<=/)\w+',text)
for s in servers:
   print(s.group())




