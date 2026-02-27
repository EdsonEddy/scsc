x = int(input())
for _ in range(x):
    n, k = map(int, input().split())
    for _ in range(k):
        s= 0
        y = n
        while y > 0:
            s =s+ y% 10
            y=y//10
        while s>= 10:
            y = s
            s= 0
            while y > 0:
                s=s+y % 10
                y=y//10
        n=n//10
        n = int(str(s) + str(n))
    print(n)