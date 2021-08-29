# start from 3.6
# we have 'String interpolation, f-string'
name='joe'
s=f"Hey {name}"
print(s)

# support expression
a=100
b=200
print(f'{a+b+100:10d}')

f=34.567
print(f'{f:.2f}')

d=100
print(f'{d:10d}')
print(f'{d:010d}')

s='abc'
print(f'{s:10s}')

# template string
from string import Template
errno=100
templ_string = 'Hey $name, there\'s a $error error!'
t=Template(templ_string).substitute(name=name, error=hex(errno))
print(t)
