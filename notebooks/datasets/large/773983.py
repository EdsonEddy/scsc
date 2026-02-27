def gauss(n):
    return (n * (n + 1)) // 2

def main():
    arr = [0] * 500
    arr[1] = 1
    veces = 4
    suma = 5
    
    for i in range(2, 200):
        arr[i] = gauss(veces)
        veces += suma
        suma += 2
    
    final = [0] * 500
    veces = 4
    suma = 5
    final[1] = 1
    
    for i in range(2, 200):
        valor = gauss(veces)
        veces += suma
        suma += 2
        valor -= arr[i - 1]
        valor -= final[i - 1]
        final[i] = valor
    
    tt = int(input())
    for _ in range(tt):
        x = int(input())
        if x == 1:
            print(1)
        else:
            print(f"{final[x - 1]}+{final[x]}")

if __name__ == "__main__":
    main()
