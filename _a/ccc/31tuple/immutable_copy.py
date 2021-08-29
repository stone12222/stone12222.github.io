"""
tuple is immutable
"""
t=1,2,3
t1=4,5,6
t2=t+t1
print(t2)

t3=sorted(t2)
print(tuple(t3))
