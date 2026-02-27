def suma(n):
    b=n%10
    n=n//10
    s=(f"({n}, {b})")    
    n=n+(b*5)
    return(s,n)
s=int(input())
for i in range(s):
    n=int(input())
    final=[]
    while True:
        if n>81:
            s,n=suma(n)
            final.append(s)
            
        else:
            break
    final1="".join(final)
    if n%7==0:
        res="correcto"
    else:
        res="incorrecto"
    print(f"{final1} {n} {res}")