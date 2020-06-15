

def fibonacci():
    x = 1
    y = 1
    yield 1
    yield 1
    while(True):
        yield x + y
        x,y = y, x+y

gen = fibonacci()

print(type(gen))

for i in range(10):
    print(next(gen))

