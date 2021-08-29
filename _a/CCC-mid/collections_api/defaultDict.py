from collections import defaultdict

timeDict=defaultdict(int)

print(timeDict[2])
print(type(timeDict))
print(isinstance(timeDict,dict))

t=defaultdict(bool)
print(t[2])

t=defaultdict(list)
print(t[2])
