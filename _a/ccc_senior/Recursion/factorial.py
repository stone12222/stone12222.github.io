'''
1 1 2 3 5 8 ...

f(x)
x=1, x=2    f(x)=1
x>2         f(x)=f(x-2)+f(x-1)

'''

def fibonacci(x, times):
   print('   '*times+'call',x)
   if x == 1 or x == 2:
       print('   ' * times+'return', 1)
       return 1
   else:
       r1=fibonacci(x-2,times+1)
       r2=fibonacci(x-1,times+1)
       print('   ' * times+'return', r1+r2)
       return r1+r2
print(fibonacci(6, 1))
