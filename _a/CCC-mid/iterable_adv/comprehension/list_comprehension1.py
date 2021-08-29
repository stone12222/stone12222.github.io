# import time
# s=time.time()
# for i in range(1000000):
#     l=[]
#     for e in range(1,6):
#         l.append(e)
#     # print(l)
# e=time.time()
# print(e-s)
#
# # syntax sugar
# s = time.time()
# for i in range(1000000):
#     l=[e for e in range(1,6)]
# e=time.time()
#     # print(l)
#
# print(e-s)

#
l = [e-2 for e in range(1, 6) if e>3]
print(l)

#
twod=[[(a,b) for a in range(3)] for b in range(3)]
print(twod)

'''
*****
*****
*****
'''
twod=[['*' for i in range(5)] for j in range(3)]
twod[0][0]='a'
print(twod)

for e in twod:
    print(id(e))

twod=[['*' for i in range(3)]]*3
twod[0][0]='a'
print(twod)
for e in twod:
    print(id(e))

