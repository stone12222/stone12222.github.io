"""
because tuple is immutable:

good performance
use it as keys
shared by multiple program
"""
t=1,2,3
t1=4,5,6
t2=t+t1
print(t2) # ok

# t2[0]=100
# sorted return a list
print(sorted(t2,reverse=True))

#
m={}
m[t]=100

# tuple doesn't have any apis
# for changing the tuple

# why?
# not allow people to change
# for performance

# process, thread
# java, c

#
l=(1,2,(2,3))
m[100]=200
print(m)
"""
{
    (1, 2, 3): 100, 
    100: 200
}
"""