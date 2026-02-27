from math import log10
casos=int(input())
for i in range(casos):
    n,k=map(int,input().split())
    for casos in range(k):
        numero=n
        while log10(numero)>=1:
            suma=0
            while numero>0:
                suma+=numero%10
                numero=numero//10
            numero=suma
        n=n//10
        n=numero*pow(10,int(log10(n)+1))+n
    print(n)