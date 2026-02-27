def sus(n):
    if n==1:
        return "1"
    else:
        return f"{(n-1)**3}+{n**3}"
T = int(input())
for i in range(T):
    n = int(input())
    print(sus(n))