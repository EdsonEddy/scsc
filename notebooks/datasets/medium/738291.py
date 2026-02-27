def suma_digitos(n):
    return sum(int(d) for d in str(n))
def raiz_digital(n):
    if n == 0:
        return 0
    return 9 if n % 9 == 0 else n % 9
t = int(input())
resultados = []
for _ in range(t):
    x, k = map(int, input().split())
    potencia = x ** k
    resultado = raiz_digital(potencia)
    resultados.append(resultado)
for res in resultados:
    print(res)
