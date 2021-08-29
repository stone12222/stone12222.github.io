# Ivan -> Kevin
# a collection of key-value pairs
# create
d={}
d={
   "jeffery":"Luke",
   "Ivan":"Kevin",
   "Kevin":"Nick",
   "Nick":None
}
print(type(d))

# read
print(d['jeffery'])
print(d.values())
print(d.keys())
print(d.items())

# for key in d.keys():
#    print(key)
for key in d:
   print(key)
for value in d.values():
   print(value)

'''
jeffery -> Luke
Ivan -> Kevin
Kevin -> Nick
Nick -> None
'''
for k in d:
   print(k,'->',d[k])
for name,neighbour in d.items():
   print(name,'->',neighbour)

# update
d['Luke']='Napu'
d['Napu']='Ivan'
print(d)

d['Luke']='Napu Sun'
d['Napu Sun']='Ivan'

# Jeffery -> Luke -> Napu -> Ivan -> Kevin -> Nick -> None
curr='jeffery'
while True:
    print(curr,'->',end=' ')
    curr=d[curr]
    if curr==None:
       print(curr)
       break

# delete
del d['Napu Sun']
print(d.pop('Ivan'))
print(d)
print(d.popitem())

# d.clear()

# query
print('Ivan' in d)
print('Ivan' in d.values())
print(len(d))

#
d={
    1:2,
    2:3,
    3:4,
    4:2
}
dd={}
for k,v in d.items():
    if v in dd:
        dd[v]=[dd[v],k]
    else:
        dd[v]=k
print(dd)



