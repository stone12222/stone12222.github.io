# defensive programming
def printAge(age):
    assert age > 0,'age<=0'
    print('your age is', age)

try:
    printAge(-20)
except AssertionError as a:
    print('error:',a)
