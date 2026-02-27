casos = int(input())
for _ in range(casos):
    # Leer n y k
    n, k = input().split()
    n = str(n)
    k = int(k)
    for _ in range(k):
        suma = int(n[0])
        for digito in n[1:]:
            suma += int(digito)
        while suma >= 10:
            suma = sum(int(digito) for digito in str(suma))
        n = n[:-1] #eliminamos el ultimo digito
        n = str(suma) + n
    print(n)