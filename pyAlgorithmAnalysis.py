import time

def create_tokens_1():
    l = []
    for i in range(1000):
        l = l + [i]
    return l
    

def create_tokens_2():
    l = []
    for i in range(1000):
        l.append(i)
    return l

time_0 = time.time()
tokens_1 = create_tokens_1()
time_1 = time.time()
tokens_2 = create_tokens_2()
time_2 = time.time()

print(time_2 - time_1 > time_1 - time_0)