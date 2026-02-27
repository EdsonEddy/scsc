n = int(input())
for _ in range(n):
    a = int(input())
    if a==1 or a ==0 or a%2!=0:
        print("Cualquiera")
    else:
        s = (a * (a+1))/2
        if s%2==0:
            print("Par")
        else:
            print("Impar")