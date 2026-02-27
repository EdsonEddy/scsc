def sum_dig(n):
    while n >= 10:
        n = sum(int(digito) for digito in str(n))
    return n
    
def cambio(n, dig):
    n=[int(digito) for digito in str(n)]
    k=[dig]
    cam=k+n[:len(n)-1]
    return(int(''.join(map(str, cam))))

casos=int(input())
for _ in range(casos):
    n, k=map(int,input().split())
    for i in range(k):
        d=sum_dig(n)
        c=cambio(n,d)
        n=c
    print(c)    