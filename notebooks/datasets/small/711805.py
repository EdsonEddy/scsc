from collections import deque
def contar_lugares_accesibles(matriz, fila_inicial, col_inicial):
    filas = len(matriz)
    columnas = len(matriz[0])
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cola = deque([(fila_inicial, col_inicial)])
    visitado = set()
    visitado.add((fila_inicial, col_inicial))
    contador = 0
    while cola:
        fila, columna = cola.popleft()
        contador += 1
        for d_f, d_c in direcciones:
            n_fila, n_columna = fila + d_f, columna + d_c
            if (0 <= n_fila < filas and 0 <= n_columna < columnas and
                matriz[n_fila][n_columna] == '.' and
                (n_fila, n_columna) not in visitado):
                visitado.add((n_fila, n_columna))
                cola.append((n_fila, n_columna))
    return contador
def main():
    while True:
        x, y = map(int, input().strip().split())
        if x == 0 and y == 0:
            break
        matriz = [input().strip() for _ in range(x)]
        for i in range(x):
            if '@' in matriz[i]:
                fila_inicial = i
                col_inicial = matriz[i].index('@')
                break
        resultado = contar_lugares_accesibles(matriz, fila_inicial, col_inicial)
        print(resultado)
if __name__ == "__main__":
    main()