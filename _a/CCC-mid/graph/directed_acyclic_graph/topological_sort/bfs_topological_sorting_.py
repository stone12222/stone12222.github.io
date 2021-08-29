"""
1. call your friend
2. Call me at work
3. Call your grandma
4. Do your Math homework
5. Feed the dog
6. watch Television
"""

"""
??????
"""

# graph_tasks = { "Do your Math homework" : ["watch Television","call your friend"],
#                 "Call your grandma" : ["Do your Math homework"],
#                 "Call me at work" : ["call your friend"],
#                 "Feed the dog" : ["Call me at work"],
#                 "watch Television":[],
#                 "call your friend":[]}

graph_tasks ={1:[4,7],
    2:[1],
    3:[4,5],
    4:[],
    5:[4],
    6:[2],
    7:[]}

def top_bfs(start_node):
    queue = [start_node]
    stack = []
    while queue:
        node = queue.pop(0)
        if not node.visited:
            node.visited = True
            stack.append(node)
            for c in node.children:
                queue.append(c)
        else:
            # node's ordering should be lowered because previously visited.
            adjustedNode = stack.remove(node)
            stack.append(adjustedNode)

    stack.reverse()
    return stack

print(top_bfs(graph_tasks))
