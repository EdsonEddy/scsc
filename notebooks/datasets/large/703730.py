T = int(input())
for _ in range(T):
    N = int(input())
    if N % 2 == 1:
        print("Cualquiera")
    else:
        if (N // 2) % 2 == 0:
            print("Par")
        else:
            print("Impar")