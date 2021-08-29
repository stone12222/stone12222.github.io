# Any object can be tested for truth value,

# The following values are considered false:
#
# for number: 0, 0.0 etc
# for string: ''
# for boolean: False
# None
# for collection: [],(),{}

# instance: condition-if-else __nonzero__() or __len__() return 0 or False

# All other values are considered true -- so objects of many types are always true.

# example:
# get user input
# condition-if-else user doesn't input anything, print 'try again'
# condition-if-else user input something, print 'pass'

n=input()
if n:
    print('You typed',n)
else:
    print('You did not type anything')
