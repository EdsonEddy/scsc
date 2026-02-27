def determinar_paridad_suma(N):
    if N == 1:
        return "Cualquiera"
    elif N % 2 == 1:
        return "Cualquiera"
    elif N % 4 == 0:
        return "Par"
    else:
        return "Impar"

num_casos = int(input())
for _ in range(num_casos):
    N = int(input())
    print(determinar_paridad_suma(N))