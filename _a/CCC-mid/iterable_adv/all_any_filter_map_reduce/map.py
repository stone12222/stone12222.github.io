# map (transform 1 element to another)
# result=map(func, sequence)
def double(number):
    return number*2

l=[1,2,3]
doubled_list = map(double, l)
print('print map 1st: ',list(doubled_list))
print('print map 2nd: ',list(doubled_list))

# map returns an iterator, which you can only iterate over once.
# I want to iterate it more than once
doubled_list = map(double, l)
doubled_list=list(doubled_list)
print(doubled_list)
print(doubled_list)

# map with lambda
result=map(lambda n:n*2, [1,2,3])
print(list(result))

# map simplify string join
l=[1,2,3,4]
print(''.join(map(str,l)))
print(''.join([str(e) for e in l]))

"""
map vs comprehension
1. map save memory by return a iterator
2. map function can do more complex steps 
3. comprehension is readable and simple
4. map can easily reuse existing functions such as str
"""
