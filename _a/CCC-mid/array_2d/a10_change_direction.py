def change_direction(d, turn):
    final_dir=d
    if turn=='R':
        final_dir+=90
    elif turn=='L':
        final_dir-=90
    return final_dir%360

start=90 #
print(change_direction(90,'L'))

















