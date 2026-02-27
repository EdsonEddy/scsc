def sucesion(n):
    if n == 1:
        return "1"
    else:
        a = (n-1) ** 3
        b = n ** 3
        return f"{a}+{b}"
T = int(input())
for _ in range(T):
    n = int(input())
    print(sucesion(n))