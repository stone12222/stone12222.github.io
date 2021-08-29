def warshall(pages):
   table={}

   for a in urls:
       table[a]={}
       for b in urls:
           table[a][b]=0

   #
   for url,others in pages.items():
       for other in others:
           table[url][other]=1
   #
   for k in urls:
       for i in urls:
           for j in urls:
               if i!=j:
                   table[i][j]=table[i][j] or (table[i][k] and table[k][j])
   return table

n=int(input())

import re

pages={}
urls=set()
for _ in range(n):
 url=input()
 pages[url]=set()
 urls.add(url)

 while True:
     line=input()
     if line=='</HTML>':
         break

     #
     matches=re.findall('"(.+?)"',line)
     for m in matches:
         pages[url].add(m)
         urls.add(m)
         print('Link from',url,'to',m)

#
table=warshall(pages)

while True:
 a=input()
 if a=='The End':
     break
 b=input()
 #
 if table[a][b]:
     print('Can surf from',a,'to',b+'.')
 else:
     print('Can\'t surf from',a,'to',b+'.')




'''
3
http://ccc.uwaterloo.ca
<HTML> <TITLE>This is the CCC page</TITLE>
Hello there boys
and girls.  <B>Let's</B> try <A HREF="http://abc.def/ghi"> a
little
problem </A>
</HTML>
http://abc.def/ghi
<HTML> Now is the <TITLE>time</TITLE> for all good people to program.
<A HREF="http://www.www.www.com">hello</A><A HREF="http://xxx">bye</A>
</HTML>
http://www.www.www.com
<HTML>
<TITLE>Weird and Wonderful World</TITLE>
</HTML>
http://ccc.uwaterloo.ca
http://www.www.www.com
http://www.www.www.com
http://ccc.uwaterloo.ca
The End

Link from http://ccc.uwaterloo.ca to http://abc.def/ghi
Link from http://abc.def/ghi to http://www.www.www.com
Link from http://abc.def/ghi to http://xxx
Can surf from http://ccc.uwaterloo.ca to http://www.www.www.com.
Can't surf from http://www.www.www.com to http://ccc.uwaterloo.ca.

'''






