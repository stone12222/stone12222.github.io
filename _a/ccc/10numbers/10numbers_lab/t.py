a=int(input())
print(a)

b=a-20*(a//20)
c=b-10*(b//10)
d=c-5*(c//5)
e=d-2*(d//2)

print('$20:',(a//20))
print('$10:',(b//10))
print('$5 :',(c//5))
print('$2 :',(d//2))
print('$1 :',e)

