casos=int(input())
for _ in range(casos):
    entrada=input().strip().split()
    n=entrada[0]
    k=int(entrada[1])
    for _ in range(k):
        suma=sum(int(digito) for digito in n)
        while suma>=10:
            suma=sum(int(d) for d in str(suma))
        n=n[:-1]
        n=str(suma)+n
    print(n)