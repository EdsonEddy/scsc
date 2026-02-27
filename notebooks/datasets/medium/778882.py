def generar_fibonacci_hasta_limite(limite):
    fib = [1, 2]
    while fib[-1] + fib[-2] <= limite:
        fib.append(fib[-1] + fib[-2])
    return fib

def convertir_a_base_fibonacci(n, fib):
    resultado = ""
    usado = False  
    for f in reversed(fib):
        if f <= n:
            resultado += '1'
            n -= f
            usado = True
        elif usado:
            resultado += '0'
    return resultado

def procesar_entrada():
    import sys
    fib = generar_fibonacci_hasta_limite(10**12)
    for linea in sys.stdin:
        n = int(linea.strip())
        print(convertir_a_base_fibonacci(n, fib))

if __name__ == "__main__":
    procesar_entrada()
