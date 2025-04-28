def primos(z):
    x=0
    for i in range(1,z+1):
        if (z%i==0):
            x=x+1
    if (x!=2):
        return False
    else:
        return True


a=int(input())
for j in range(a):
    p=0
    n=0
    k=int(input())
    while p<1000:
        p=k*(2**n)+1
        z=p
        n+=1
        if primos(z)==True:
            print(p)
            break