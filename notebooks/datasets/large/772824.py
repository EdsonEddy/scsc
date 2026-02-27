t=int(input())
for _ in range(t):
    n=int(input())
    a=(n-1)**3
    b=n**3
    if(n==1):
        print(1)
    else:
        print(f"{a}+{b}") 
