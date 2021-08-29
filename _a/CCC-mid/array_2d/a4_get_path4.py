import a1_getposition_rowcol as position

li = [['A', 'B', 'C', 'D', 'E', 'F'],
      ['G', 'H', 'I', 'J', 'K', 'L'],
      ['M', 'N', 'O', 'P', 'Q', 'R'],
      ['S', 'T', 'U', 'V', 'W', 'X'],
      ['Y', 'Z', ' ', '-', '.', 'enter']]

def getPath(start, end):
    r1, c1 = position.getPosition(start)
    r2, c2 = position.getPosition(end)
    print(start)

    while True:
        if r1 < r2:
            r1 += 1
        elif r1>r2:
            r1 -= 1
        if c1 < c2:
            c1 += 1
        elif c1>c2:
            c1 -= 1
        print(li[r1][c1])
        if (r1 == r2 and c1 == c2):
            break

getPath("H", "W")
