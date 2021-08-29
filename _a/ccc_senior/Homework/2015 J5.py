results={}
def eat(n, k, min):
   if (n,k,min) in results:
       return results[(n,k,min)]

   if k == 1:
       return 1

   result = 0
   for i in range(min, n // k + 1):
       result += eat(n - i, k - 1, i)
   results[(n,k,min)]=result
   return result

n = int(input())
k = int(input())
print(eat(n, k, 1))


