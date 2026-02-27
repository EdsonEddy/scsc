for i in range(int(input())):
    n=int(input())
    p2=n-1
    suma=0
    suma2=0
    for j in range(n):
        numero=str(input().strip())
        suma+=int(numero[j])
        suma2+=int(numero[p2])
        p2-=1
    print(suma-suma2)