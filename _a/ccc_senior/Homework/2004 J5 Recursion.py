# level, width, x=[int(e) for e in input().split()]
total_level=2
width=27
x=19

def grow(line,level):
   if level==total_level+1:
       lines.append(line)
       return

   x1,y1,x6,y6,dir=line

   p1=x1,y1
   p6=x6,y6
   # 5 new lines
   if dir=='up':
       w=(x6-x1)//3
       p2=(x1+w,y1)
       p3=(x1+w,y1+w)
       p4=(x1+2*w,y1+w)
       p5=(x1+2*w,y1)
       l1=(*p1,*p2,'up')
       l2=(*p2,*p3,'left')
       l3=(*p3,*p4,'up')
       l4=(*p4,*p5,'right')
       l5=(*p5,*p6,'up')
   elif dir == 'left':
       w=(y6-y1)//3
       p2 = x1, y1 + w
       p3 = x1 - w, y1 + w
       p4 = x1 - w, y1 + 2 * w
       p5 = x1, y1 + 2 * w
       l1 = *p1, *p2, 'left'
       l2 = *p2, *p3, 'down'
       l3 = *p3, *p4, 'left'
       l4 = *p4, *p5, 'up'
       l5 = *p5, *p6, 'left'
   elif dir == 'right':
       w=(y1-y6)//3
       p2 = x1, y1 - w
       p3 = x1 + w, y1 - w
       p4 = x1 + w, y1 - 2 * w
       p5 = x1, y1 - 2 * w
       l1 = *p1, *p2, 'right'
       l2 = *p2, *p3, 'up'
       l3 = *p3, *p4, 'right'
       l4 = *p4, *p5, 'down'
       l5 = *p5, *p6, 'right'
   elif dir == 'down':
       w=(x1-x6)//3
       p2 = x1 - w, y1
       p3 = x1 - w, y1 - w
       p4 = x1 - 2 * w, y1 - w
       p5 = x1 - 2 * w, y1
       l1 = *p1, *p2, 'down'
       l2 = *p2, *p3, 'right'
       l3 = *p3, *p4, 'down'
       l4 = *p4, *p5, 'left'
       l5 = *p5, *p6, 'down'
   for l in [l1,l2,l3,l4,l5]:
       grow(l,level+1)

lines=[]
line=0,1,width,1,'up'
grow(line,1)

for line in lines:
   print(line)


