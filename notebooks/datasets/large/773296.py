T = int(input()) 
for _ in range(T):
    n = int(input())  
    if n == 1:
        print("1") 
    else:
        print(f"{(n-1)**3}+{n**3}") 