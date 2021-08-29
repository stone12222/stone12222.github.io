class Data(object):
    # use %s or !s
    def __str__(self):
        return 'str_data'

    # use %r，%a or !r
    def __repr__(self):
        return '打印repr_data'

print('%s %r' % (Data(), Data()))
print('{0!s} {0!r}'.format(Data()))

print('%s %a' % (Data(), Data()))

"""
dict
"""

data = {'first': 'Hodor', 'last': 'Hodor!'}

print('%(first)s %(last)s' % data)
print('{first} {last}'.format(**data))

