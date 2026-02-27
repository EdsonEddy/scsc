# Movimientos posibles: arriba, abajo, izquierda, derecha
direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def explorar_area(mapa, visitado, fila, col, max_filas, max_columnas):
    # Marcamos la posición actual como visitada
    visitado[fila][col] = True
    lugares_accesibles = 1  # Contamos el lugar actual

    # Movemos a las 4 direcciones posibles
    for desplazamiento_fila, desplazamiento_col in direcciones:
        nueva_fila = fila + desplazamiento_fila
        nueva_col = col + desplazamiento_col

        # Verificamos los límites y si el lugar es accesible ('.') y no visitado
        if 0 <= nueva_fila < max_filas and 0 <= nueva_col < max_columnas:
            if not visitado[nueva_fila][nueva_col] and mapa[nueva_fila][nueva_col] == '.':
                # Continuamos la búsqueda en el nuevo lugar
                lugares_accesibles += explorar_area(mapa, visitado, nueva_fila, nueva_col, max_filas, max_columnas)

    return lugares_accesibles

def resolver():
    while True:
        # Leemos las dimensiones del mapa
        filas, columnas = map(int, input().split())
        if filas == 0 and columnas == 0:
            break  # Fin de entrada cuando ambos son cero

        # Leemos el mapa de la ciudad
        ciudad = [list(input().strip()) for _ in range(filas)]

        # Encontrar la posición inicial del '@' y convertirla en '.'
        pos_inicial_fila = pos_inicial_col = -1
        for i in range(filas):
            for j in range(columnas):
                if ciudad[i][j] == '@':
                    pos_inicial_fila, pos_inicial_col = i, j
                    ciudad[i][j] = '.'  # Convertimos '@' en lugar visitable

        # Creamos una matriz de visitados para no repetir lugares
        ya_visitado = [[False] * columnas for _ in range(filas)]

        # Llamamos a DFS desde la posición inicial y contamos los lugares accesibles
        resultado = explorar_area(ciudad, ya_visitado, pos_inicial_fila, pos_inicial_col, filas, columnas)

        # Imprimimos el resultado
        print(resultado)

if __name__ == "__main__":
    resolver()
