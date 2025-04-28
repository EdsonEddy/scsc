from math import sqrt
def primo(x):
    if x!=1:
        for k in range(2,x,1):
            if x%k==0:
                r='false'
                break
        else:
            r='true'
    else:
        r='false'
    return r





while 1:
    n=int(input())
    for i in range(n):
        k = int(input())
        for j in range(k):
            n=(k*2**j)+1
            if primo(n)=='true':
                print(n)
                break
