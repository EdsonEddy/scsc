from math import sqrt

def primo(n):
    n=n
    a=0
    for i in range(2,int(sqrt(n)+1),1):
        if 0 == n % i:
            a=1
            break
    return a



while True:
    n=int(input())
    for i in range(n):
        a=1
        c=0
        s=int(input())
        while a==1:
            r =( s * (2 ** c)) + 1
            a = primo(r)
            c+=1
        print(r)
