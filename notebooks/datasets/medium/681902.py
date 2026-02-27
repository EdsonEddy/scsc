import heapq
import sys


def process_input(n, lista):
    q = []
    for x in lista:
        heapq.heappush(q, x)

    total = 0

    while len(q) > 1:
        costo_actual = heapq.heappop(q)
        costo_actual += heapq.heappop(q)
        total += costo_actual
        heapq.heappush(q, costo_actual)

    return total


for line in sys.stdin:
    n = int(line.strip())
    if n <= 0:
        break
    lista = list(map(int, input().split()))
    result = process_input(n, lista)
    print(result)
