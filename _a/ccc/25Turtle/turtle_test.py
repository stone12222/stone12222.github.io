# ipython: shell, repl(read, evaluate, print, loop)
# pygame

$ ipython
Python 3.8.5 (default, Jul 21 2020, 10:42:08)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.18.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 1+1
Out[1]: 2

In [2]: print('hello')
hello

In [3]: import turtle

In [4]: me=turtle.Turtle()

In [5]: me.shape('turtle')

In [6]: me.color('red')

In [7]: me.color('blue')

In [8]: me.forward(100)

In [9]: me.left(90)

In [10]: me.forward(100)

In [11]: me.clear()

In [12]: me.home()

In [13]: me.clear()

In [14]: for i in range(6):
    ...:     me.forward(100)
    ...:     me.left(60)
    ...:


In [15]:

In [15]: me.right(10)

In [16]: for i in range(6):
    ...:     me.forward(100)
    ...:     me.left(60)
    ...:

In [17]: me.clear()

In [18]: for i in range(36):
    ...:     for j in range(6):
    ...:         me.forward(100)
    ...:         me.left(60)
    ...:     me.right(10)
    ...:


In [19]:

In [19]: me.penup()

In [20]: me.forward(120)

In [21]: me.forward(120)

In [22]: me.begin_fill()

In [23]: me.circle(10)

In [24]: me.end_fill()

In [25]: me.home()

In [26]: me.circle(300)

In [27]: me.pendown()

In [28]: me.circle(200)

In [29]: me.penup()

In [30]: me.goto(300,300)

In [31]: exit