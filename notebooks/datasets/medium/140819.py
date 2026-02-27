def primos(x):
 ListaP=[2]
 i=3
 while i <= x:
     SWPrimo=True
     limite=int(i**(0.5)+1)
     for primo in ListaP:
         if i%primo==0:
             SWPrimo=False
             break
         elif primo >= limite:
             break
     if SWPrimo:
         ListaP.append(i)
     i+=2
 return ListaP

j=primos(1000000)
x=0
while x != -1:
    x = int(input())
    if x <=1000000:
        imprimir=str(x)+' = '
        for i in range (0,78498):
           c=0
           if j[i]<=x:
               if x%j[i]==0:
                   while x%j[i]==0:
                       c=c+1
                       x=x//j[i]
                   imprimir=imprimir+str(j[i])
                   if c > 1:
                       imprimir=imprimir+'^'+str(c)
                   imprimir=imprimir+'*'
           else:
               break
        if x!=-1:
            w=list(imprimir)
            del(w[-1])
            print(''.join(w))
