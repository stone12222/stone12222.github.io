g={
    1:[4,7],
    2:[1],
    4:[],
    5:[4],
    6:[2],
    3:[4,5],
    7:[]}

# step 1
in_degree={node:0 for node in g}
for neighbour in g.values():
    for node in neighbour:
        in_degree[node]+=1
# print(in_degree)

# step 2
order=[]
while True:
    if not in_degree:
        break

    q = [(v, k) for k, v in in_degree.items()]
    q = sorted(q)
    print(q)

    job=q.pop(0)
    if job[0]==0:
        order.append(job[1])

        # remove from in_degree
        del in_degree[job[1]]
        #
        for neighbour in g[job[1]]:
            in_degree[neighbour] -= 1
            print(in_degree)
    else:
        break

print(order)

