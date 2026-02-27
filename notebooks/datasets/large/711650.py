def sumadigitos(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def transformar(n, k):
    n = str(n) 
    for _ in range(k):
        suma = sumadigitos(int(n))
        n = n[:-1]
        n = str(suma) + n
    
    return n
t = int(input())  
for _ in range(t):
    n, k = map(int, input().split()) 
    resultado = transformar(n, k)
    print(resultado)
