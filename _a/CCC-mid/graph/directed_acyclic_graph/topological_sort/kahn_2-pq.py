from queue import PriorityQueue

def ts(graph):
    # create in-degree table
    in_degree={n:0 for n in graph}
    for v in graph.values():
        for n in v:
            in_degree[n]+=1

    # put nodes with in-degree 0 to the queue
    q=PriorityQueue()
    for n in in_degree:
        if in_degree[n]==0:
            q.put(n)

    l=[]
    while q.qsize()>0:
        # before pop, sort it
        n1=q.get()
        l.append(n1)
        # remove dependency by updating in-degree table
        for ns in graph[n1]:
            in_degree[ns]-=1
            if in_degree[ns]==0:
                q.put(ns)

    if len(l)!=len(graph):
        return []
    else:
        return l

graph={1:[4, 7],
       2:[1],
       3:[4,5],
       4:[],
       5:[4],
       6:[2],
       7:[]}

order=ts(graph)
print(order)


