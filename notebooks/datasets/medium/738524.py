def solve(x, k):
    x %= 9
    if x == 0: x = 9
    a = pow(x, k, 9)
    for _ in range(200):
        a = a % 9
        if a == 0: a = 9
    return a if a != 0 else 9

t = int(input())
for _ in range(t):
    x, k = map(int, input().split())
    print(solve(x, k))
