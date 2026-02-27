for _ in range(int(input())):
    n = int(input())
    a = (n - 1) * (n - 1) * (n - 1)
    b = n * n * n
    
    if n == 1: print(1)
    else:
        print(str(a) + '+' + str(b))    