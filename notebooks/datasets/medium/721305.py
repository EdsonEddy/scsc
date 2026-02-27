def generar_fibonacci(hasta):
    fib = [1, 2]
    while fib[-1] + fib[-2] <= hasta:
        fib.append(fib[-1] + fib[-2])
    return fib

def representar_en_base_fibonacci(n):
    fib = generar_fibonacci(n)
    representacion = []
    for numero in reversed(fib):
        if numero <= n:
            representacion.append('1')
            n -= numero
        else:
            if representacion:
                representacion.append('0')
    return ''.join(representacion)


try:
    while True:
        n = int(input())
        print(representar_en_base_fibonacci(n))
except EOFError:
    pass 