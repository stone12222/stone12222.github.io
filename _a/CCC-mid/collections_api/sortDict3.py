def add(a,b):
    return a+b

c=add(100,200)
print(c)

# anonymous function
l=lambda a,b:a+b
c=l(100,200)
print(c)

#
d={
    'dog':400,
    'email':500,
    'apple':800,
    'cat':300,
    'broad':200
}

# sort key
for key in sorted(d.keys()):
    print(key,d[key])

# sort by key
dd={k:d[k] for k in sorted(d.keys())}
print(dd)

# sort by values
dd={k:v for k,v in sorted(d.items(),key=lambda a:a[1])}
print(dd)




