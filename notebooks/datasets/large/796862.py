def es_primo(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n=int(input())
for _ in range(n):
    m=int(input())
    cont=0
    maxp=0
    for i in range(1,501):
        if es_primo((i**2)-i+m):
            cont+=1
        else:
            if cont>maxp:
                maxp=cont
            cont=0
    if cont>maxp:
        maxp=cont
    print(f"{m}: {maxp}")