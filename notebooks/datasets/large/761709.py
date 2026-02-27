def funcion_redondear(numero, decimales=2):
    return int(numero * 100 + 0.5) / 100

def calcular_porcentaje_de_vocales(cadena):
    vocales = 'aeiou'
    total = len(cadena)
    porcentajes = {}
    for vocal in vocales:
        cnt = cadena.count(vocal)
        porcentaje = (cnt * 100) / total
        porcentajes[vocal] = funcion_redondear(porcentaje)

    return porcentajes

def procesar_casos_de_prueba(casos):
    c = 1
    for caso in casos:
        resultado = calcular_porcentaje_de_vocales(caso)
        print(f'Caso {c}:')
        c += 1
        for fruta, porcentaje in resultado.items():
            print(f"{fruta}= {porcentaje:.2f}")

if __name__ == "__main__":
    t = int(input())
    casos = []
    for _ in range(t):
        cadena = input()
        casos.append(cadena)

    procesar_casos_de_prueba(casos)