from math import log10
t = int(input())
for _ in range(t):
    n, k=map(int, input().split())
    for sit in range(k):
        num = n
        while log10(num) >=1:
            suma = 0
            while num > 0:
                suma += num % 10
                num //= 10
            num = suma
        n=n//10
        n=num*pow(10,int(log10(n)+1))+n
    print(n)