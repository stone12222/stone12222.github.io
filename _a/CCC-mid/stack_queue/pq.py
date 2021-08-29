from queue import PriorityQueue

pq=PriorityQueue()

#
pq.put((0,(0,0)))
pq.put((7,(3,1)))
pq.put((3,(2,4)))
pq.put((2,(1,7)))

for e in pq.queue:
    print(e)

'''
heapq
'''
import heapq
pq=[]
heapq.heappush(pq,(0,(0,0)))
heapq.heappush(pq,(7,(0,0)))
heapq.heappush(pq,(3,(0,0)))
heapq.heappush(pq,(2,(0,0)))

for e in pq:
    print(e)
