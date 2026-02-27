casos=int(input())
for i in range(casos):
    n=int(input())
    res=[]
    while n>81:
        d=n%10
        iz=n//10
        res.append((iz,d))
        n=iz+(d*5)
    
    #
    print(*res,sep='',end=' ')
    if n%7==0:
        print(f'{n} correcto')
    else:
        print(f'{n} incorrecto')