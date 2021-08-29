# join
l=[1,2,3]
l2=[4,5,6]
l3=l+l2
print(l3)

# copy
l4=l
l.append(100)
print(l4)

l=[1,2,3]
l4=l[:]
l.append(100)
print(l4)

# zip
l1=[1,2,3]
l2=['joan','kenna','jiaqi']
l3=zip(l1,l2)
print(list(l3))

# use 'copy' module
import copy
l=[3,4,5]
l1=copy.copy(l)
print(l1)
l.append(6)
print(l1)
l2=copy.deepcopy(l)
print(l2)
