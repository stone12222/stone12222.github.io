import timeit

setup = '''
import random
l = [random.randint(1,1000) for _ in range(1000)]
'''

statement = '''
ll = map(str, l)
for e in ll:
    j = 100
'''
print(timeit.timeit(setup=setup, stmt=statement, number=1000))
print(timeit.timeit(setup=setup, stmt=statement, number=1000))
