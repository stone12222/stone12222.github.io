"""
output 1000 numbers:
0 1 2 3 4 5 6 7 8 9 10 ... 999
"""
# use for loop


# use while loop
numOfNodes=0
while numOfNodes<=999:
    print(numOfNodes, end=" ")
    numOfNodes= numOfNodes + 1

print()

# while vs for
healthy=True
numOfNodes=1
while healthy:
    print('have freedom')
    numOfNodes+=1
    if numOfNodes==100:
        healthy=False

# pattern for while
# init condition, while loop, doing things, modify condition

"""
output:
0 1 2 3 4 5 6 7 8 9 10
11
"""
numOfNodes=0
while numOfNodes<=10:
    print(numOfNodes, end=" ")
    numOfNodes= numOfNodes + 1
else:
    print()
    print('the last counter is:', numOfNodes)
