'''
'''
import random
X=[random.randint(0,1000) for _ in range(10000)]
X.sort(reverse=True)
Y=[random.randint(0,1000) for _ in range(10000)]
Y.sort(reverse=True)

# X=[8,8,4,4,4,3,3,3,1]
# Y=[9,9,8,8,6,5,5,4,3]
def getDis(X,Y):
  max_dis=0

  for i in range(len(X)):
      for j in range(i,len(Y)):
          if Y[j]>=X[i]:
              dis=j-i
              max_dis=max(dis,max_dis)
  return max_dis

def getDis1(X,Y):
   max_dis=0
   for i in range(len(X)):
       l = i
       h = len(Y) - 1
       target=X[i]
       while True:
           m = (h + l) // 2

           if l > h:
               max_dis=max(max_dis,h-i)
               break

           if target <= Y[m]:
               l = m + 1
           elif target > Y[m]:
               h = m - 1
   return max_dis

import time
s=time.time()
dis=getDis(X,Y)
e=time.time()
print(e-s)
print(dis)

s=time.time()
dis=getDis1(X,Y)
e=time.time()
print(e-s)
print(dis)

# print('The maximum distance is',dis)