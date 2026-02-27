
def digito_raiz(n):
    if n == 0:
        return 9
    return n


def a_201(x, k):
    
    
    potencia_mod9 = pow(x, k, 9)
    
    
    return digito_raiz(potencia_mod9)


def main():
    
    t = int(input())
    
    
    for _ in range(t):
        x, k = map(int, input().split())
        print(a_201(x, k))

if __name__ == "__main__":
    main()
