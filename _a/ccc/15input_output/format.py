n=111

print(n)
print("%10d" % n)
print("%010d" % n)
print("%010s" % "abc")

n='111'
print(n)
print(n.zfill(10))

#
print('{0:<10}{1:<10}'.format(100,200))
print('{0:_<10}{1:<10}'.format(300,400))
print('{0:_>10}{1:<10}'.format(300,400))

# https://pyformat.info/