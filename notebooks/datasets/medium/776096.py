import sys
for linea in sys.stdin:
    n = int(linea)
    if n == -1:
        break
    temp = n
    factores = []
    i = 2
    while i * i <= temp:
        cnt = 0
        while temp % i == 0:
            cnt += 1
            temp //= i
        if cnt:
            factores.append((i, cnt))
        i = 3 if i == 2 else i + 2
    if temp > 1:
        factores.append((temp, 1))
    salida = []
    for p, e in factores:
        salida.append(f"{p}" + (f"^{e}" if e > 1 else ""))
    print(f"{n} = {'*'.join(salida)}")