# l=[
    # [17, 24, 1, 8, 15],
    # [23, 5, 7, 14, 16],
    # [4, 6, 13, 20, 22],
    # [10, 12, 19, 21, 3],
    # [11, 18, 25, 2, 9]
   # ]

l=[
    [68,81,  94,  107,  120,  1,  14,  27,  40,  53,  66],
[80,  93,  106,  119,  11,  13,  26,  39,  52,  65,  67],
[92,  105,  118,  10,  12,  25,  38,  51,  64,  77,  79],
[104,  117,  9,  22,  24,  37,  50,  63,  76,  78,  91],
[116,  8,  21,  23,  36,  49,  62,  75,  88,  90,  103],
[7,  20,  33,  35,  48,  61,  74,  87,  89,  102,  115],
[19,  32,  34,  47,  60,  73,  86,  99,  101,  114,  6],
[31,  44,  46,  59,  72,  85,  98,  100,  113,  5,  18],
[43,  45,  58,  71,  84,  97,  110,  112,  4,  17,  30],
[55,  57,  70,  83,  96,  109,  111,  3,  16,  29,  42],
[56,  69,  82,  95,  108,  121,  2,  15,  28,  41,  54]
]

rows=len(l)
cols=len(l[0])

sum_r=0
for row in range(rows):
    for col in range(cols):
       sum_r+=l[row][col]
    print('row:',sum_r)
    sum_r=0

sum_c=0
for col in range(cols):
    for row in range(rows):
       sum_c+=l[row][col]
    print('col:',sum_c)
    sum_c=0

# backward diagonal
sum_bd=0
for i in range(rows):
    sum_bd+=l[i][i]
print('backward diagonal',sum_bd)

# forward diagonal
sum_fd=0
for i in range(rows):
    sum_fd+=l[i][rows-1-i]
print('forward diagonal',sum_fd)
