'''
create
'''
a=set()
print(a)
a={1,2,3}
print(a)
a.add(4)
print(a)
a.add(100)
print(a)

a.add(100)
print(a)

#
s1={1,2,3}
s2={2,3,4}
s3=s1&s2 # intersection
s4=s1|s2 # union
s5=s1-s2 # difference
s6=s2-s1
s7=s1^s2
print(s3)
print(s4)
print(s5)
print(s6)
print(s5|s6)
print(s7)

# set
print(100 in a)
result=100 not in a
print(result)

#
s1={1,2}
s2={1,2,3}
print(s1>s2)


