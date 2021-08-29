import random
import time
l = [random.randint(1,100) for _ in range(100000)]
#print(l)

s = time.time_ns()
ll = [str(e) for e in l]
e = time.time_ns()
print('com:', e-s)

# map() transfer 1 collection to another
s = time.time_ns()
ll = map(str, l)
e = time.time_ns()
print('map:', e-s)

###
s = time.process_time_ns()
ll = [str(e) for e in l]
for e in ll:
    j = 100
e = time.process_time_ns()
print('com:', e-s)

s = time.process_time_ns()
ll = map(str, l)
for e in ll:
    j = 100
e = time.process_time_ns()
print('map:', e-s)

###
s = time.perf_counter_ns()
ll = [str(e) for e in l]
for e in ll:
    j = 100
e = time.perf_counter_ns()
print('com:', e-s)

s = time.perf_counter_ns()
ll = map(str, l)
for e in ll:
    j = 100
e = time.perf_counter_ns()
print('map:', e-s)