l=['_']

row=l*8
print(row)

"""
[
    ['_', '_', '_', '_', '_', '_', '_', '_']
    ['_', '_', '_', '_', '_', '_', '_', '_']
    ['_', '_', '_', '_', '_', '_', '_', '_']
    ['_', '_', '_', '_', '_', '_', '_', '_']
    ['_', '_', '_', '_', '_', '_', '_', '_']
    ['_', '_', '_', '_', '_', '_', '_', '_']
    ['_', '_', '_', '_', '_', '_', '_', '_']
    ['_', '_', '_', '_', '_', '_', '_', '_']
]
"""
board=[row]*8

for row in board:
    print(*row)
