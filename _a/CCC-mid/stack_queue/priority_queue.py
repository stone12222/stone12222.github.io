# heapq implementation has O(log n) time
# for insertion and extraction of the smallest element.
# Note that heapq only has a min heap implementation
import heapq

import time
s=time.time()
customers = []
for i in range(100000):
    heapq.heappush(customers, (2, "Harry"))
    heapq.heappush(customers, (3, "Charles"))
    heapq.heappush(customers, (1, "Riya"))
    heapq.heappush(customers, (4, "Stacy"))

while customers:
     heapq.heappop(customers)

e=time.time()
print(e-s)

# PriorityQueue uses the same heapq implementation internally
# and but slower than heapq, because
# it is synchronized, so it supports concurrent processes.
from queue import PriorityQueue

customers=PriorityQueue()
s=time.time()
for i in range(100000):
    customers.put((2, "Harry"))
    customers.put((3, "Charles"))
    customers.put((1, "Riya"))
    customers.put((4, "Stacy"))

for i in range(customers.qsize()):
# while customers:
    customers.get()

e=time.time()
print(e-s)

# while customers.qsize():
#      print(customers.get())

