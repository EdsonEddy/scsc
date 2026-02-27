def fib_base(n):
    fib = [1, 2]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    fib.pop()
    res = []
    for f in reversed(fib):
        if f <= n:
            res.append('1')
            n -= f
        else:
            res.append('0')
    return ''.join(res)

import sys
for line in sys.stdin:
    print(fib_base(int(line)))