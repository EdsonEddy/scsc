def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def secuencia_primos(C):
    max_longitud = 0
    longitud_actual = 0
    
    for n in range(1, 1000):
        valor = n * n - n + C
        if valor > 0 and es_primo(valor):
            longitud_actual += 1
        else:
            if longitud_actual > max_longitud:
                max_longitud = longitud_actual
            longitud_actual = 0
    
    if longitud_actual > max_longitud:
        max_longitud = longitud_actual
    
    return max_longitud
N = int(input())
for _ in range(N):
    C = int(input())
    print(f"{C}: {secuencia_primos(C)}")