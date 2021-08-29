li=[['A','B','C','D','E','F'],
  ['G','H','I','J','K','L'],
  ['M','N','O','P','Q','R'],
  ['S','T','U','V','W','X'],
  ['Y','Z',' ','-','.','enter']]

def getPos(char):
  for x in li:
     if char in x:
        pos=[li.index(x),x.index(char)]
        return pos

def getPath(start,end):
  r1,c1=getPos(start)
  r2,c2=getPos(end)
  print(li[r1][c1],end=" ")
  
  while (r1,c1)!=(r2,c2):
     if r1>r2:
        r1-=1
        print(li[r1][c1],end=" ")
     elif r1<r2:
        r1+=1
        print(li[r1][c1],end=" ")
     elif c1<c2:
        c1+=1
        print(li[r1][c1],end=" ")
     elif c1>c2:
        c1-=1
        print(li[r1][c1],end=" ")
getPath("J","A")
print()
getPath("A","J")



