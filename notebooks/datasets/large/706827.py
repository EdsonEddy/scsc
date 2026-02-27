def cubo(n):
    return n ** 3

def resultados(T, casos):
    resultados = []
    suma_anterior = 0
    for n in casos:
        if n > 1:
            resultado = f"{cubo(n-1)}+{cubo(n)}"
        else:
            resultado = f"{cubo(n)}"
        resultados.append(resultado)
    return resultados

T = int(input().strip())
casos = [int(input().strip()) for _ in range(T)]

resultados = resultados(T, casos)
for resultado in resultados:
    print(resultado)