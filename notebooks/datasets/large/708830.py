t = int(input())
for _ in range(t):
    n=int(input())
    if n==1:
        print(1)
    else:
        segundo=n*n*n
        n-=1
        primero=n*n*n
        print(f"{primero}+{segundo}")