import heapq


def main():
    while True:
        n = int(input())
        if n == 0:
            break

        # Leer toda la línea y convertir los elementos en enteros
        numeros = list(map(int, input().split()))

        # Crear una cola de prioridad (min-heap) usando heapq
        q = []
        for num in numeros:
            heapq.heappush(q, num)

        c = 0
        while len(q) > 1:
            a = heapq.heappop(q)  # Extraer el menor elemento
            b = heapq.heappop(q)  # Extraer el siguiente menor elemento
            x = a + b  # Sumar ambos elementos
            c += x  # Acumular el costo
            heapq.heappush(q, x)  # Insertar la suma de vuelta en la cola

        print(c)


if __name__ == "__main__":
    main()
