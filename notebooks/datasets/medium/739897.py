def raiz_digital(num):
    if num == 0:
        return 0
    return 1 + (num - 1) % 9  

def procesar_casos(casos_de_prueba):
    for base, exponente in casos_de_prueba:
        raiz_base = raiz_digital(base)
        resultado_raiz = raiz_digital(raiz_base ** exponente)
        print(resultado_raiz)

n = int(input())
casos_de_prueba = [tuple(map(int, input().split())) for _ in range(n)]

procesar_casos(casos_de_prueba)
