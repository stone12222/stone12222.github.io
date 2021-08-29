'''
# prove
# n=O(n-log2(n))
# f(n)<2*g(n-log2(n)) when n>6
'''
def n2(x):
   return x**2

def n2_n(x):
   return x**2-x*10

# draw line
for n in range(1,50000):
   f=n2(n)
   g=n2_n(n)
   diff=f-g
   print("%.3f, %.3f" % (diff,diff/f))