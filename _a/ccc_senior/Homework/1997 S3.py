teams=[]
for i in range(int(input())):
    teams.append(int(input()))

for i in teams:
    r = 0
    u = i
    o = 0
    e = 0
    print("Round " + str(r) + ":", u, "Undefeated,", o, "one-loss,", e,"eliminated")
    while (r<8):
        r += 1
        e += o//2
        if o%2 == 0:
            o = o//2 + u//2
        else:
            o = o//2 + u//2 + 1
        u = u//2
        if u < 0: u = 0
        if o < 0: o = 0
        print("Round " + str(r) + ":", u, "Undefeated,", o, "one-loss,", e, "eliminated")

        if(u == 1 and o == 1):
            u = 0
            o = 2
            r += 1
            print("Round " + str(r) + ":", u, "Undefeated,", o, "one-loss,", e, "eliminated")
        if(u==0 and o == 2):
            o = 1
            e += 1
            r += 1
            print("Round " + str(r) + ":", u, "Undefeated,", o, "one-loss,", e, "eliminated")
        if e == i-1:
            break;