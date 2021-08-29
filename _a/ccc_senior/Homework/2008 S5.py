def check(list):
    winner = 0
    while True:
        if list[0] >= 2 and list[1] >= 1 and list[3] >= 2:
            list[0] -= 2
            list[1] -= 1
            list[3] -= 2
            winner += 1
        elif list[0] >= 1 and list[1] >= 1 and list[2] >= 1 and list[3] >= 1:
            list[0] -= 1
            list[1] -= 1
            list[2] -= 1
            list[3] -= 1
            winner += 1
        elif  list[2] >= 2 and list[3] >= 1:
            list[2] -= 2
            list[3] -= 1
            winner += 1
        elif list[1] >= 3:
            list[3] -= 1
            winner += 1
        elif list[0] >= 1 and list[3] >= 1:
            list[0] -= 1
            list[3] -= 1
            winner += 1
        else:
            return winner
            break


def runGame(particles):
    particles = list(particles)
    a,b,c,d = particles[0],particles[1],particles[2],particles[3]
    l = [a,b,c,d]

    winner = check(l)
    if winner % 2 == 0:
        return("Roland")
    else:
        return("Patrick")


games = []
a = int(input())
for i in range(a):
    games.append([int(x) for x in input().split()])

print(games)

for i in range(a):
    print(i, runGame(games[i]))
