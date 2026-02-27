def obtener_raiz_digital(numero):
    return numero if numero == 0 else 9 if numero % 9 == 0 else numero % 9

def calcular_resultado(a, b):
    potencia = a ** b
    return obtener_raiz_digital(potencia)

def procesar_entradas(casos):
    resultados = []
    for caso in casos:
        a, b = caso
        resultados.append(calcular_resultado(a, b))
    return resultados

if __name__ == "__main__":
    total = int(input())
    entradas = [tuple(map(int, input().split())) for _ in range(total)]
    resultados = procesar_entradas(entradas)
    
    for res in resultados:
        print(res)
