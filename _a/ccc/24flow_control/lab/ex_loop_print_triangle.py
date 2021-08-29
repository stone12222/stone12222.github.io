'''
 *********
  *******
   *****
    ***
     *
'''
# 1st step
print('*'*(9-0))
print('*'*(9-2))
print('*'*(9-4))
print('*'*(9-6))
print('*'*(9-8))

# 2nd step
n=int(input()) # 9
t=n
while True:
    print(' '*((t-n)//2)+'*'*n)
    n=n-2
    if n<0:
        break

#
for i in range(t,0,-2):
    print(' '*((t-i)//2)+'*'*i)
