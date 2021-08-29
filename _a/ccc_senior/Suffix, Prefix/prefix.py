ex = "- - 3 + 2 1 9".split()

ex.reverse()
s = []

for e in ex:
    if e.isnumeric():
        s.append(e)
    else:
        a=s.pop()
        b=s.pop()
        c = e+a+b
        s.append(c)

print(s)