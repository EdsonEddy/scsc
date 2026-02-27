def fibonacci_representation(n):
    fib = [1, 2]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])

    fib_rep = []
    for f in reversed(fib):
        if f <= n:
            fib_rep.append(1)
            n -= f
        else:
            if fib_rep:
                fib_rep.append(0)

    return ''.join(map(str, fib_rep))

while True:
    try:
        n = int(input())
        print(fibonacci_representation(n))
    except EOFError:
        break
