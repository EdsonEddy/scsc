s=int(input())
for i in range(s): 
    n=int(input())
    if n==1:
        print("1")
    else:
        b=(n-1)**3
        c=n**3
        print(f"{b}+{c}")