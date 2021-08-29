# crud: create, read, update, delete

# no position (but by key), no duplicate
# Changed in version 3.7: Dictionary order is guaranteed to be insertion order.
# This behavior was implementation detail of CPython from 3.6.
"""
create
"""
d={}

# a collection of key-value pairs
d={
    'js':'javascript',
    'py':'python',
    'html':'hypertext markup language'
}
print(d)

d=dict(js='javascript',py='python')
print(d)

"""
read
"""
print(d['js'])
print(d.get('js'))

"""
update
"""
d['js']='javascript is a wild animal'
print(d)

"""
add
"""
d['java']='java is not coffee'
print(d)

"""
delete
"""
del d['java']
# return value
x = d.pop('js')
print(x)

"""
delete a last item since 3.7 LIFO order is guaranteed.
"""
i = d.popitem()
print(i)

d.clear()
# here here here
"""
get keys
"""
d = {1: 'one',
     2: 'two',
     3: 'three'}
keys = d.keys()
print(list(keys))

"""
get arbitrary key
"""
print(next(iter(d.keys())))

"""
get values
"""
values = d.values()

"""
query
"""
print(1 in d)

# fromkeys
print(dict.fromkeys((1,2,3),'a'))


