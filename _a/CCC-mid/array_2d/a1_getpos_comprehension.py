l=[
   ['A','B','C','D','E','F'],
   ['G','H','I','J','K','L'],
   ['M','N','O','P','Q','R'],
   ['S','T','U','V','W','X'],
   ['Y','Z',' ','-','.','enter']
]

def getPos(c):
       rid,row=[(rid,r) for rid,r in enumerate(l) if c in r][0]
       col=row.index(c)
       return (rid,col)

# print(getPos("H"))


