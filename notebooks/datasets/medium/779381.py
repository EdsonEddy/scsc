def fibonacci_base(n):
    fib = [1, 2]
    while fib[-1] <= n:
        fib.append(fib[-2] + fib[-1])

    fib_rep = []
    for i in range(len(fib) - 1, -1, -1):
        if fib[i] <= n:
            fib_rep.append('1')
            n -= fib[i]
        else:
            if fib_rep: 
                fib_rep.append('0')

    return ''.join(fib_rep)

while True:
    try:
        n = int(input())
        print(fibonacci_base(n))
    except EOFError:
        break
