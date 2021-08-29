ex = '1 2 3 * + 4 -'.split()

s = []

for e in ex:
    if e.isnumeric():
        s.append(e)
    else:
        a = s.pop()
        b = s.pop()
        c = eval(str(b) + e + str(a))
        s.append(c)
print(*s)