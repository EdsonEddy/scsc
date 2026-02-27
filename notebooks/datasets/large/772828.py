t=int(input())
ans=[]
for i in range(t):
    dato=int(input())
    #for j in range(1, dato+1):
    if dato==1:
        ans.append(f"{dato**3}")
    else:
        ans.append(f"{(dato-1)**3}+{dato**3}")
for i in range(t):
    print(ans[i])