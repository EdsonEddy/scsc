A=int(input())
CC=0
X=0
while X<=A:
    CC=0
    EE=0
    z=1
    k=int(input())
    X=0
    m=k*(2**EE)+z
    te=1
    CC=CC+1
    if CC==A:
        break
    else:
        if m>10**4:
            print("-1")
        else:
            while m<10**4:
                while te<=m:
                    dig=m%te
                    if dig==0:
                        X=X+1
                        te=te+1
                    else:
                        te=te+1
                if X==2:
                    print(m)
                    break
                else:
                    X=0
                    te=1
                    EE=EE+1
                    m=k*(2**EE)+1
            if m>10**4:
                print("-1")