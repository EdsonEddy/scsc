import sys
import math

for l in sys.stdin:
    n = int(l)
    if n == -1:
        break
    x = n
    f = []
    i = 2
    while i * i <= x:
        c = 0
        while n % i == 0:
            n //= i
            c += 1
        if c == 1:
            f.append(str(i))
        elif c > 1:
            f.append(str(i) + '^' + str(c))
        i += 1
    if n > 1:
        f.append(str(n))
    print(str(x) + ' = ' + '*'.join(f))