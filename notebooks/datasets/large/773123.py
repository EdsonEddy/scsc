casos=int(input())
lista=[]
for i in range(casos):
    n=int(input())
    if n==1:
        lista.append(str(1))
    else:
        lista.append(str((n-1)**3)+'+'+str(n**3))
    
for i in lista:
    print(i)