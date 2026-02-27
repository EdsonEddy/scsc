def calcular_sucesion(n):
    if n == 1:
        return "1"
    else:
        anterior = (n - 1) ** 3  # (n-1)^3
        actual = n ** 3          # n^3
        return f"{anterior}+{actual}"
T = int(input())
resultados = []
for _ in range(T):
    n = int(input())
    resultados.append(calcular_sucesion(n))
for resultado in resultados:
    print(resultado)