T = int(input())

resultados = []

for _ in range(T):
    n = int(input())
    
    if n == 1:
        resultado = "1"
    else:
        anterior = (n - 1) ** 3
        actual = n ** 3
        resultado = f"{anterior}+{actual}"
    
    resultados.append(resultado)

for res in resultados:
    print(res)