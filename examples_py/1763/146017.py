P=int(input())
for i in range ( P):
    Y=int(input())
    SW=True
    for h in range (10000):
        U=Y*2**h+1
        if(U==2 or 2**(U-1)%U==1):
            SW=False
            break
    if(SW):
       print(-1)
    else:
      print(U)
