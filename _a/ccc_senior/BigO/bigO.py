#Complexity Analysis / Algorithm Analysis
#Constant 0(1)
#Polynomial
#P problem

n = 800
print(n)
print(n)

#2^3 = 8    log(8) = 3
#8 >> 4 >> 2(3 times) = log(8)
#10 = 3*3 = 3*log(8)
#o(3log(n)+1) = o(log(n))
while True:
    print(n)
    n=n//2
    if n == 1:
        break

# linear o(2n) = o(n)
n = 8
for i in range(2*n):
    pass

#o(nlogn)
print("####")
n = 8
c = 1
for i in range(n):
    n=8
    while True:
        print(c)
        c+=1
        print(n) #3
        n = n//2 #3
        if n == 1: #4
            break

#o(n^2): Quadratic
for i in range(n):
    for j in range(k):
        pass

#o(n^3): Cubic
for i in range(n):
    for j in range(n):
        for k in range(n):
            pass

#Non polynomial
#0(2^n): Exponential
#Fibonacci Sequence: fib(6) = 1 1 2 3 5 8 13

#o(n!): Factorial
#5! = 5*4*3*2*1

#n^n
#graph
