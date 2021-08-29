line1 = "ABCDEFG"
line2 = "HIJKLMN"
line3 = "OPQRSTU"

# convert string to 1 dimension list
"""
[
 ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
 ['H', 'I', 'J', 'K', 'L', 'M', 'N'],
 ['O', 'P', 'Q', 'R', 'S', 'T', 'U']
]

as a list not a string
"""

print('[',list(list(line1)), list(line2), list(line3),']',sep='\n')
# print(list(["A",'B','C','D','E'],["H",'I','J','K','L','M','N']),sep="\n")
# print(" [", "\n", list(line1), ",", "\n", list(line2), ",", "\n", list(line3), ",", "\n", "]")
