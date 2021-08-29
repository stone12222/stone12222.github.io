def change_direction(d,turns):
    final_dir=d
    for turn in turns:
        if turn=='R':
            final_dir+=90
        elif turn=='L':
            final_dir-=90
    return final_dir%360

turns=['R','R']
print(change_direction(90,turns))
