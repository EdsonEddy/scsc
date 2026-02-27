t = int(input())
for _ in range(t):
    n = int(input())
    s1 = 0
    s2 = 0
    for i in range(n):
        f = input().strip()
        s1 += int(f[i])
        s2 += int(f[n - 1 - i])
    d = s1 - s2
    print(d)