m = int(input())

def verificar(resul):
    if resul <= 1:
        return False
    for i in range(2, int(resul**0.5) + 1):
        if resul % i == 0:
            return False
    return True

for i in range(m):
    k = int(input())
    maximo = 0

    # Probar todos los posibles inicios de n
    inicio = 1
    while inicio <= 500:
        cont = 0
        n = inicio

        while n <= 500:
            resul = n * n - n + k
            if verificar(resul):
                cont += 1
                n += 1
            else:
                break

        if cont > maximo:
            maximo = cont

        inicio += 1

    print(f"{k}: {maximo}")

