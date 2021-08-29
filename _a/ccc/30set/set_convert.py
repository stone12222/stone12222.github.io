"""
string -> set
"""
s="123"
char_set=set(s)

"""
list -> set
"""
l=[1,2,3]
s=set(l)

"""
set -> list
"""
l=list(s)
print(l)

"""
copy
"""
s1=set(s)
