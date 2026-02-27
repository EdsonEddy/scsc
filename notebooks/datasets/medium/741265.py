def suma_digitos(n):
    if n == 0:
        return 0
    return 9 if n % 9 == 0 else n % 9

def obtener_a201(x, k):
    potencia = x ** k
    a = suma_digitos(potencia)
    if a < 10:
        return a 
    for _ in range(200):
        a = suma_digitos(a)
        if a < 10:
            break 
    return a

if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):
        x, k = map(int, input().strip().split())
        resultado = obtener_a201(x, k)
        print(resultado)