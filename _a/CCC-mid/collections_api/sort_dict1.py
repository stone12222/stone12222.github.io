d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# sort by key
d1=sorted(d)
print(d1)

d2=sorted(d.items())
print(d2)

# sort by value
d3={k:v for k,v in sorted(d.items(),key=lambda e:e[1])}
print(d3)

# sort by length of key
