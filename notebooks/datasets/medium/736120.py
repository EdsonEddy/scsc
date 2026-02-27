def raiz_digital(n):
    if n == 0:
        return 0
    elif n % 9 == 0:
        return 9
    else:
        return n % 9

def procesar_caso(x, k):
    resultado = pow(x, k)
    return raiz_digital(resultado)

n = int(input()) 
for _ in range(n):
    x, k = map(int, input().split())
    print(procesar_caso(x, k))
