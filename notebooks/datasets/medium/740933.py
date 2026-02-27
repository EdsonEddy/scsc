def raiz_digital(n):
    if n == 0:
        return 0
    return 9 if n % 9 == 0 else n % 9

def a201(x, k):
    # Calculamos la raiz digital de x
    raiz_x = raiz_digital(x)
    
    # Calculamos la potencia k de esa raiz digital
    resultado = pow(raiz_x, k, 9)  # Calcular (raiz_x ^ k) % 9
    
    # Si el resultado es 0, la raiz digital es 9 (excepción de la fórmula)
    return 9 if resultado == 0 else resultado

# Leer el número de casos de prueba
n = int(input())

# Procesar cada caso
for _ in range(n):
    x, k = map(int, input().split())
    print(a201(x, k))