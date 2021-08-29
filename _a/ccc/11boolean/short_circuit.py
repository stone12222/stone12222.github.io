# https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

# 'and is short-circuit operator, so it only evaluates
# the second argument condition-if-else the first one is True.'
print(100>1000 and 100/0)

# 'or is a short-circuit operator, so it only
# evaluates the second argument condition-if-else the first one is False'
print(100>20 or 100/0)


