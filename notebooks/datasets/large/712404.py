def suma_entre_a_y_b(a, b, numeros):
    suma = 0
    for numero in numeros:
        if a <= numero <= b:
            suma += numero
    return suma

def procesar_casos_de_prueba():
    import sys
    input = sys.stdin.read
    datos = input().splitlines()
    
    i = 0
    while i < len(datos):
        a, b = map(int, datos[i].split())
        numeros = list(map(int, datos[i + 1].split()))
        resultado = suma_entre_a_y_b(a, b, numeros)
        print(resultado)
        i += 2
procesar_casos_de_prueba()