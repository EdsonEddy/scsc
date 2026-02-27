def suma_digitos(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num

def proceso(n, k):
    n = str(n)  
    for _ in range(k):
        suma = suma_digitos(int(n))
        n = n[:-1]
        n = str(suma) + n
        
    return n

casos = int(input()) 
for _ in range(casos):
    n, k = map(int, input().split())  
    resultado = proceso(n, k)  
    print(resultado)