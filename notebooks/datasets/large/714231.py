for _ in range(int(input())):
    n=int(input())
    if n%2==1:
        print("Cualquiera")
    elif (n//2)%2==0:
        print("Par")
    else:
        print("Impar")
