def upside_down_asterix_triangle(i, t=0):
    if i == 0:
        return 0
    else:
        print(' ' * ( t + 1 ) + '*' * ( i * 2 - 1 ))
        return upside_down_asterix_triangle( i - 1, t + 1 )

upside_down_asterix_triangle(5)

def asterix_triangle(i, t=0):
    if i == 0:
        return 0
    else:
        print(' ' * ( i + 1 ) + '*' * ( t * 2 + 1 ))
        return asterix_triangle( i - 1, t + 1 )

asterix_triangle(5)

def create_pyramid(rows):
    for i in range(rows):
        print((' ' * ( rows- i - 1 ) + '*' * ( 2 * i + 1)))

print((create_pyramid(5)))

def create_upside_down_pyramid(rows):
    for i in reversed(list(range(rows))):
        print((' ' * ( rows- i - 1 ) + '*' * ( 2 * i + 1)))

print((create_upside_down_pyramid(5)))
