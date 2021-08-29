'''
4
Before 02/03/04, 02/03/05, but not after December 19, 99,
there was a rehash of the 55.34.02 meeting.  A date, like November 15,
95 cannot traverse two lines, nor can it be surrounded by alphabetics
or numerics like this:  78November 01, 88, or 6801/12/03, or 02/03/04x.

1
April  8,  8   May 01,01  June 30, 89, December 01/02/03

January|February|March|April|May|June|July|August|September|October|November|December
'''
def fix_year(year):
   year=int(year)
   if year<=24:
       year+=2000
   else:
       year+=1900
   return str(year)

# get data, clean data, analysis data, data mining(data science, Machine learning), apply pattern
def isValid(day,month):
   if month.isnumeric():
       month=int(month)
   day=int(day)
   if month in [1,3,5,7,8,10,12,'January','March','May','July','August','October','December'] and 0<day<32:
       return True
   elif month in [4,6,9,11,'April','June','September','November'] and 0<day<31:
       return True
   elif month in [2,'February'] and 0<day<30:
       return True
   return False

import re
n=int(input())
for i in range(n):
   line=input()

   matches=list(re.finditer('(?<!\w)(\d\d)/(\d\d)/(\d\d)(?!\w)',line))
   for m in matches[::-1]:
       s,e=m.span()
       day=m.group(1)
       month=m.group(2)
       if isValid(day,month):
           year=m.group(3)
           year=fix_year(year)
           date=day+'/'+month+'/'+year
           line=line[:s]+date+line[e:]

   matches=list(re.finditer('(?<!\w)(January|February|March|April|May|June|July|August|September|October|November|December) (\d\d), (\d\d)(?!\w)',line))
   for m in matches[::-1]:
       s,e=m.span()
       month=m.group(1)
       day=m.group(2)
       if isValid(day,month):
           year=m.group(3)
           year=fix_year(year)
           date=month+' '+day+', '+year
           line=line[:s]+date+line[e:]

   matches=list(re.finditer('(?<!\w)(\d\d)\.(\d\d)\.(\d\d)(?!\w)',line))
   for m in matches[::-1]:
       s,e=m.span()
       month=m.group(2)
       day=m.group(3)
       if isValid(day,month):
           year = m.group(1)
           year=fix_year(year)
           date=year+'.'+month+'.'+day
           line=line[:s]+date+line[e:]
   print(line)



