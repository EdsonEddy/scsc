def t(n, k):
    for _ in range(k):
        s = sum(int(digit) for digit in str(n))
        while s >= 10:
            s = sum(int(digit) for digit in str(s))
        n = str(s) + str(n)[:-1]
    return int(n)
c = int(input())
for _ in range(c):
    n, k = map(int, input().split())
    print(t(n, k))