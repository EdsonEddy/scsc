def fibonacci_sequence_up_to(n):
    fib = [1, 2]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    if fib[-1] > n:
        fib.pop()
    return fib

def fibonacci_base(n):
    fib = fibonacci_sequence_up_to(n)
    result = []
    used = False
    for f in reversed(fib):
        if n >= f:
            result.append('1')
            n -= f
            used = True
        elif used:
            result.append('0')
    return ''.join(result) if result else '0'

import sys

for line in sys.stdin:
    line = line.strip()
    if line:
        number = int(line)
        print(fibonacci_base(number))