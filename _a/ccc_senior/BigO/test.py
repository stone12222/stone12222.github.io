# Big O cares about the worst case

n = 5
if n < 2:
    print(n)
elif n < 4:
    for i in range(n):
        pass
else:
    for i in range(n):
        for j in range(n):
            pass

# Ignore the constant
# o(n)
for i in range(n):
    print(100)
    print(100)

# Ignore the lower order, keep the dominate order
# o(n+n^2) = o(n^2)
for i in range(n):
    pass
for i in range(n):
    for j in range(n):
        pass

#o(n^3+nlog(n)+n^2+n) = 0(n^3)