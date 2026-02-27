T = int(input())
for _ in range(T):
    n = int(input())
    if n == 1:
        print(1)
    else:
        a = (n - 1) ** 3
        b = n ** 3
        print(f"{a}+{b}")
