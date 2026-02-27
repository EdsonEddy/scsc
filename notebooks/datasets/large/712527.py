def suma_digitos(num):
   
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num
t = int(input())

for _ in range(t):
    
    n, k = map(int, input().split())
    n = str(n)  

    for _ in range(k):
        
        suma = suma_digitos(int(n))

        
        n = n[:-1]

       
        n = str(suma) + n
    print(n)