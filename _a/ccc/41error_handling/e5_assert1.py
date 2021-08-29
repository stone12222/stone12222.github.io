def setAge(age):
    # defensive programming
    assert age>0,'age should >0'

    print('age ',age,'is set')

setAge(0)

"""
debugging skills:
print()
set breakpoint, then step through
try-except
assert
"""
