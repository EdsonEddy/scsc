n=int(input())
for _ in range(n):
    m=int(input())
    s=0
    if(m%2!=0):
        print("Cualquiera")
    else:
        for j in range(1,m+1):
            s=s+j
        if(s%2==0):
            print("Par")
        else:
            print("Impar")