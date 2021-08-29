"""
string -> char list
"""
s='abc'
cl=list(s)
print(cl)

# char list -> string
ss='%%'.join(cl) # a,b,c
print(ss)
