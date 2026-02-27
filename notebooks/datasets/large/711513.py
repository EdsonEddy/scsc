def sigRegla(n, k):
    for i in range(k):
        n = int(f"{9 if n%9==0 else n%9}{n//10}")
    return n
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(sigRegla(n,k))