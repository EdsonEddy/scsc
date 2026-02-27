from sys import stdin
def input():
    return stdin.readline().strip()

def prop(n:int)->int:
    return (sum(list(map(int,list(str(n)))))%9)**2

limite=1000000 +5
numeros=[True]*limite
primos=[]
for i in range(2,limite):
    if numeros[i]:
        primos.append(i)
        for j in range(i*i,limite,i):
            numeros[j]=False

n=int(input())
while n!=-1:
    
    
    auxn=n
    punt=0
    ans=[]
    print(f"{n} = ",end="")
    while primos[punt]*primos[punt]<=auxn and n>1:
        cont=0
        while n%primos[punt]==0:
            cont+=1
            n//=primos[punt]
        if cont==1:
            ans.append(str(primos[punt]))
        elif cont>1:
            ans.append(f"{primos[punt]}^{cont}")

        punt+=1
    if n!=1:ans.append(n)
    print(*ans,sep="*")
    n=int(input())


    
    
    