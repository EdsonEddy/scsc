def cs(n):
    if n == 1:
        return "1"
    a = (n - 1) ** 3 
    b = n ** 3 
    return f"{a}+{b}"
T = int(input().strip())
for _ in range(T): 
    n = int(input().strip())
    print(cs(n))     