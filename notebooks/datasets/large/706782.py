def encontrar_siguiente(n):
    num = n ** 3
    num_anterior = (n - 1) ** 3
    if num_anterior == 0:
        return num
    else:
        return f"{num_anterior}+{num}"

f = int(input())

for _ in range(f):
    n = int(input())
    print(encontrar_siguiente(n))
