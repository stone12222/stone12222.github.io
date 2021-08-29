# ordered key-value pairs
d={
    2:'b',
    1:'a',
    3:'c'
}

# 3.7
dd={k*2:v*3 for k,v in d.items()}
print(dd)


