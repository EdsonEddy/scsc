from sys import stdin

def base_fibonacci(n):
    fib = [1, 2]

    while fib[-1] <= n: fib.append(fib[-1] + fib[-2])
    fib.pop()
    res = []
    for f in reversed(fib):
        if f <= n:
            res.append(1)
            n -= f
        else: res.append(0)
    return ''.join(map(str, res))

for i in stdin:
    i = int(i)
    print(base_fibonacci(i))
