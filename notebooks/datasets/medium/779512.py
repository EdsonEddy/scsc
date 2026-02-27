fibonacci = [1, 2]
while fibonacci[-1] + fibonacci[-2] <= 10**12:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

def base_fibonacci(n):
    resultado = ''
    usado = False
    for f in reversed(fibonacci):
        if f <= n:
            resultado += '1'
            n -= f
            usado = True
        elif usado:
            resultado += '0'
    return resultado

try:
    while True:
        linea = input()
        if linea.strip() == "":
            continue
        n = int(linea.strip())
        print(base_fibonacci(n))
except EOFError:
    pass
