ll=[
    ['16', '3', '2', '13'],
   ['5', '10', '11', '8'],
   ['9', '6', '7', '12'],
   ['4', '15', '14', '1']
]

for r in ll:
    for e in r:
        print(e,end='\t\t')
    print()

print("column->row")

for n in range(4):
    for r in ll:
        print(r[n], end='\t\t')
    print()

print('backward diagonal')
for i in range(4):
    print(ll[i][i],end="\t\t")

print('forward diagonal')

# 0, 3-0  (0,3)
# 1, 3-1  (1,2)
# 2, 3-2  (2,1)
# 3, 3-3  (3,0)
for i in range(4):
    j=3-i
    print(ll[i][j],end="\t\t")
