n=int(input())
for _ in range(n):
    a=int(input())
    r=(a-1)**3
    b=a**3
    if r==0:
        print (b)
    else:    
        print(f"{r}+{b}")