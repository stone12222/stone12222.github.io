def comp():
    l = [e for e in range(1,1000000)]

def loopFunc():
    l = []
    for i in range(1,1000000):
        l.append(i)

def main():
    comp()
    loopFunc()

import cProfile

cProfile.run('main()')