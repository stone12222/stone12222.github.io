"""
all
"""
# l=[True,True,True, False]
#
# allTrue=True
# for e in l:
#     if e!=True:
#         allTrue=False
# print(allTrue)
#
# print(all(l))

l=[1,2,3,4]
# l1=[e<100 for e in l]
# all(l1)

print(all(e<100 for e in l))

"""
any
"""
print(any(e<4 for e in l))

