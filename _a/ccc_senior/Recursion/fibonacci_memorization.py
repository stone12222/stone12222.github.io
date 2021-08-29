#fibonacci sequence = rabbit sequence

knowledge = {}

def fib(num, calls):
    if num in knowledge:
        return knowledge[num]

    if num == 1 or num == 2:
        return 1
    else:
        r = fib(num-2,calls+1) + fib(num-1,calls+1)
        knowledge[num] = r
        return r

import time
s = time.process_time()
print(fib(30,1))
e = time.process_time()
print(e-s)