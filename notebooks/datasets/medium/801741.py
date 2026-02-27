def root(n):
    res=n%9
    if res==0: return 9
    else: return res
        
def exp_bin(base,exponent):
    if exponent==0: return 1
    res=exp_bin(base,exponent//2)
    res*=res
    if exponent%2==1: res*=base
    return res
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    res=root(n)
    res=root(exp_bin(res,k))
    print(res)
