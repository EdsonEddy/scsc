limite=1000005
num=[True]*limite
num[0]=False
num[1]=False

primos=[]
for i in range(limite):
    if num[i]==True:
        primos.append(i)
        for j in range(2*i, limite,i):
            num[j]=False

#print(primos)
n=int(input())

while n!=-1:
    aux=n
    respuesta=[]
    for i in range(len(primos)):
        cont=0
        while n%primos[i]==0:
            n=n//primos[i]
            cont=cont+1
        
        if cont==1:
            respuesta.append(primos[i])
        if cont>1:
            respuesta.append(f"{primos[i]}^{cont}")
        
        if n==1:
            break
    print(f"{aux} = ",end="")
    print(*respuesta,sep="*")

    n=int(input())