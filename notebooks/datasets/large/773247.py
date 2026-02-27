t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
        continue
    print(f"{(n-1)**3}+{n**3}")