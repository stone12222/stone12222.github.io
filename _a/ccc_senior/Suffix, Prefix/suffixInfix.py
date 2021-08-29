ex = '1 + 2 * 3 - 4 + 5'.split()

q = []
s = []

'''
-1 ascending order
0 same
1 descending order
'''
1
for e in ex:
    if e.isnumeric():
        q.append(e)
    else:
        if check_order(e,s[-1]) == -1:
            s.append(e)