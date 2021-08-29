"""
it can be a generator function or generator expression
"""

# generator expression
# lazy mode
g=(x*2 for x in [1, 2, 3])
for i in g:
    print(i,end=' ')
# I can't loop the second time
for i in g:
    print(i,end=' ')
print()

# if it is used as argument for a function,
# parentheses doesn't need
sum(x for x in [1,2,3])

# vs comprehension
# a generator expression is similar to a list comprehension,
# Differences are:
'''
0. generator uses parentheses instead of brackets.
1. a list comprehension computes all of the values and stores them in memory,
2. a generator expression generates its values lazily on demand (i.e __next__()),
without storing all values in memory, and once complete, cannot be reused.
'''
l=[x*2 for x in [1, 2, 3, 4, 5]]
for i in l:
    print(i,end=' ')
