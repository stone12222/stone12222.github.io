for i in range(int(input())):
    distance = []
    b = int(input())
    x = [int(i) for i in input().split()]
    y = [int(i) for i in input().split()]

    for j in range(b):
        for h in range(b):
            if x[j] == y[b-h-1]:
                distance.append(b-h-1-j)
                break
    if len(distance) != 0:
        print("The maximum distance is",max(distance))
    else:
        print("The maximum distance is 0")