def suma_digitos(n):
   
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def proceso(n, k):
    for _ in range(k):
        
        suma = suma_digitos(n)
        
        n = n // 10
        
        n = int(str(suma) + str(n))
    return n

t = int(input())  
for _ in range(t):
   
    n, k = map(int, input().split())
    resultado = proceso(n, k)
    print(resultado)


