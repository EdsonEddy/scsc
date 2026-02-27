n = int(input())
for i in range(n):
    a = int(input())
    if a == 1:
        print("1")
    else:
        print((a-1)**3, "+", a**3, sep="")