# print diagonal
li=[
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

rows=len(li)
cols=len(li[0])

# backward diagonal
for i in range(rows):
    print(li[i][i])

print()

# forward diagonal
for i in range(rows):
    print(li[i][rows-1-i])








# backward diagonal
# print("backward diagonal")
# size=len(li)
# for i in range(size):
#     print(li[i][i])

# print("forward diagonal")
# # forward diagonal
# for i in range(size):
#     print(li[i][size-i-1])
