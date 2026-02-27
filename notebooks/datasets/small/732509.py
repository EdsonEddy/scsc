def contar_lugares(ciudad, fila, columna, visitado):
    if (fila < 0 or fila >= len(ciudad) or columna < 0 or columna >= len(ciudad[0]) or ciudad[fila][columna] == '#' or visitado[fila][columna]):
        return 0
    visitado[fila][columna] = True
    count = 1
    count += contar_lugares(ciudad, fila - 1, columna, visitado)  
    count += contar_lugares(ciudad, fila + 1, columna, visitado)
    count += contar_lugares(ciudad, fila, columna - 1, visitado)
    count += contar_lugares(ciudad, fila, columna + 1, visitado)  

    return count

if __name__ == "__main__":
    import sys
    for linea in sys.stdin:
        linea = linea.strip()
        if linea:
            x, y = map(int, linea.split())
            if x == 0 and y == 0:
                break
            ciudad = []
            posicion_inicial = (-1, -1)
            for i in range(x):
                fila = input().strip()
                ciudad.append(fila)
                if '@' in fila:
                    posicion_inicial = (i, fila.index('@'))
            visitado = [[False] * y for _ in range(x)]
            fila_inicial, columna_inicial = posicion_inicial
            resultado = contar_lugares(ciudad, fila_inicial, columna_inicial, visitado)
            print(resultado)
