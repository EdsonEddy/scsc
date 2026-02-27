t=int(input())
for i in range(t):
    n=int(input())
    if(n<=1):
        print(n)
    else:
        print(f"{(n-1)**3}+{n**3}")