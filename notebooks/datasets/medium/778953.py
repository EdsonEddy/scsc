def generar_fibonacci(h):
    fib = [1, 2]
    while fib[-1] + fib[-2] <= h:
        fib.append(fib[-1] + fib[-2])
    return fib

def representar_en_base_fibonacci(n):
    fib = generar_fibonacci(n)
    v = []
    for num in reversed(fib):
        if num <= n:
            v.append('1')
            n -= num
        else:
            if v:
                v.append('0')
    return ''.join(v)

try:
    while True:
        n = int(input())
        print(representar_en_base_fibonacci(n))
except EOFError:
    pass