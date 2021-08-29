i, l1, l2, d = int(input()), input().split(), input().split(), {}
for n in range(i):
   if l1[n] not in d.values():
       d[l1[n]] = l2[n]

print('good' if len(d.keys()) + len(d.values()) == i else 'bad')


