t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    m = []
    for _ in range(n):
        r = list(map(int, list(input().strip())))
        m.append(r)
    
    dp = sum(m[i][i] for i in range(n))
    ds = sum(m[i][n-i-1] for i in range(n))
    d = dp - ds
    
    print(d)