try:
    f=open('noexistfile')
    r=f.readlines()
    for line in r:
        print(line)
except OSError:
    print('Error 001: FileNotFound')
finally:
    print('this line will be printed anyway')
