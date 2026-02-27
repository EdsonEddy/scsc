import sys
e1 = sys.stdin.read().splitlines()
n1 = int(e1[0])
for i in range(1, n1 + 1):
    n, k = e1[i].split()
    k = int(k)
    for c in range(k):
        nn = int(n)
        while nn >= 10:
            nn = sum(int(d) for d in str(nn))
        n = n[:-1]
        n = str(nn) + n
    print(n)