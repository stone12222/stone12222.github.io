# check username, if not empty, print 'good', if empty, print 'no'

username=input()
if username!='':
    print('good')
else:
    print('your username should not be empty')

# consider 'non-empty string' as truthy value
if username:
    print('good')
else:
    print('your username should not be empty')

# what values considered as Falsey value?
# number 0
# boolean False
# string ''
# list []
# set {}
# tuple ()
# None

# check?
bool('abc')