
def fib_rec(n):
    if n == 1 or n == 2:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

print fib_rec(10)
print fib_rec(1)
print fib_rec(23)

def fib_dyn(n):
    cache = {1:1,2:1}
    if(cache.get(n) != None):
        return cache.get(n)
    else:
        cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    return cache[n]

print fib_dyn(10)
print fib_dyn(1)
print fib_dyn(23)

def fib_iter(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

print fib_iter(10)
print fib_iter(1)
print fib_iter(23)
