x=int(input())
for i in range(x):
    k=int(input())
    sw=True
    for j in range(10000):
        num=k*2**j+1
        if (num ==2 or (2**(num-1)%num)==1):
            sw=False
            break
    if sw:
        print(-1)
    else:
        print(num)