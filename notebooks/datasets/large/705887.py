import sys
casos=int(input())
cont=1
for i in range (casos):
    n=int(input())
    for j in range (1,n+1):
        if (j==1):
            aux=1
            aux2=0
        else:
            if(j==2):
                aux=1
                aux2=8
            else:
                aux=(j-1)**3
                aux2=j**3
    if(aux==1 and aux2==0):
        print(aux,sep='')
    else:
        print (aux,"+",aux2,sep='')
        