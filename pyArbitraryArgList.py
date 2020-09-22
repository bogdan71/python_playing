def func(a, *args):
    print(a)
    for arg in args:
        print(arg)

func("A", "B", "C")