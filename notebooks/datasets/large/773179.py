t = int(input())

for i in range(t):
    n = int(input())
    if n == 0:
        print(1)
        continue
    if n == 1:
        print(1)
        continue
    pri = (n - 1)**3
    seg = n**3
    print(f"{pri}+{seg}")
