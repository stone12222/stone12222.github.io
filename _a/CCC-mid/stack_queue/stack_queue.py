# stack
# Last IN, First OUT (LIFO)
l=[]
print(l)
l.append(1)
print(l)
l.append(2)
print(l)
l.append(3)
print(l)
l.pop()
print(l)
l.pop()
print(l)
l.pop()
print(l)

# queue
# First IN, First OUT (FIFO)
print('####################')
l=[]
print(l)
l.append(1)
print(l)
l.append(2)
print(l)
l.append(3)
print(l)
l.pop(0)
print(l)
l.pop(0)
print(l)
l.pop(0)
print(l)

# deque: double ended queue
print('Double ended queue')
from collections import deque
deq=deque()
'''
queue
'''
deq.append(1)
deq.append(2)
deq.append(3)

print(deq.popleft())
print(deq.popleft())
print(deq.popleft())

'''
stack
'''
deq.append(1)
deq.append(2)
deq.append(3)

print(deq.pop())
print(deq.pop())
print(deq.pop())

# priority queue use heapq
# PriorityQueue is slow, because it has code to
# do synchronize
from queue import PriorityQueue
pq=PriorityQueue()
pq.put(3)
pq.put(100)
pq.put(50)
print(pq.qsize())
print(pq.queue)
print(pq.get())
print(pq.get())

# heapq
import heapq
l=[]
heapq.heappush(l,8)
heapq.heappush(l,1)
heapq.heappush(l,5)
heapq.heappush(l,3)
print(heapq.heappop(l))
print(heapq.heappop(l))
print(heapq.heappop(l))
print(heapq.heappop(l))
