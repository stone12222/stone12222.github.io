d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# 键，值
# by key
keys=sorted(d.keys())
a={}
for k in keys:
    a[k]=d[k]
print(a)

#
print(list(d.items()))
print(sorted(d.items()))

b={k:v for k,v in sorted(d.items())}
print(b)

# by value
c={k:v for k,v in sorted(d.items(),key=lambda i:i[1])}
print(c)

# by key length
c={k:v for k,v in sorted(d.items(),key=lambda i:len(i[0]))}
print(c)



