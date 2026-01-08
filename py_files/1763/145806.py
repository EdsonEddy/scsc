def primos(z):
    a=0
    for i in range(1, z + 1):
        if (z % i == 0):
            a=a+1
    if (a!=2):
        return False
    else:
        return True

m=int(input())
for q in range(m):
    proth = 0
    n=0
    k=int(input())
    while proth<1000:
        proth=k*(2**n)+1
        z=proth
        n+=1
        if primos(z)==True:
            print(proth)
            break


       