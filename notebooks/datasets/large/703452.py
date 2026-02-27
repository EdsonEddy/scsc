for casos in range (int(input( ))):
    n = int(input())
    if n % 2 != 0:
        print("Cualquiera")
    elif (n//2)%2 != 0:
        print("Impar")
    else:
        print("Par")