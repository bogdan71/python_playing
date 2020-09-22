def f(a, b='b', c='c', type='T'):
    print("Input ", a, b, c, type)

f(1000)
f(a=1000)
f(a=1000000, c='ccc')
#f()
f(c='ccc', a=1000000)
f('happy', 'life', 'rich')
f('poor', b='happy')
#f(a=5.0, 'dead')
#f(110, a=220)
#f(actor='Johny Depp')

Solution
4

Explanation
Functions can also be called using keyword arguments of the form kwarg=value. In a function call, keyword arguments must follow positional arguments. All the keyword arguments passed must match one of the arguments accepted by the function (e.g. actor is not a valid argument for the function), and their order is not important. This also includes non-optional arguments (e.g. f(a=1000) is valid, too). No argument may receive a value more than once.

Invalid function calls:
#4 required argument missing
#8 non-keyword argument after a keyword argument
#9 duplicate value for the same argument
#10 unknown keyword argument