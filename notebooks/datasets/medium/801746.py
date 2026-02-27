t = int(input())
for _ in range(t):
    x, k = map(int, input().split())
    
    if k == 0:
        print(1)
    elif x % 9 == 0:
        print(9)
    else:
        r = pow(x % 9, k, 9)
        print(9 if r == 0 else r)