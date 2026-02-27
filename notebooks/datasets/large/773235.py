def fun(n):
    if n == 1:
        return 1
    else:
        return str((n-1)**3) + '+' + str(n**3)
        
n  = int (input())
for i in range(n):
    m = int(input())
    print(fun(m))