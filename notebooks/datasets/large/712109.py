a=int(input())
for _ in range(a):
    n,k=map(int,input().split())
    for _ in range(k):
        a = sum(int(x) for x in str (n))
        while a >= 10:
            a = sum(int(x) for x in str(a))
        n=n // 10
        n=int(str(a)+str(n))
    print(n)