a=200
exec('''
if a>50:
    print('a>50')
''')

#
file=open('test.py')
exec(file.read())

# dynamic ability: allow to config program when it's running
