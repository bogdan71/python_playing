def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def test_add():
    assert add(1, 2) == 3

def inc(x):
    return x + 1

def test_subtract():
    assert subtract(2, 1) == 1

def test_inc():
    assert inc(3) == 4