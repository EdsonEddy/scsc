def desproporcion_diagonal(matriz):
    a = len(matriz)
    dig_principal = 0
    dig_secundaria = 0
    
    for i in range(a):
        dig_principal += matriz[i][i]
        dig_secundaria += matriz[i][a - i - 1]
    
    return dig_principal - dig_secundaria

def main():
    prueba = int(input())
    
    for _ in range(prueba):
        a = int(input())
        matriz = []
        for _ in range(a):
            f = list(map(int, input().strip()))
            matriz.append(f)
        
        r = desproporcion_diagonal(matriz)
        print(r)

if __name__ == "__main__":
     main()