import math

def es_posible_cumplir_plazo(a, b):
    k = 0  
    while k < a:  
        tiempo_restante = a - k
        tiempo_construccion_optimizado = math.ceil(b / (k + 1))
        
        if tiempo_construccion_optimizado <= tiempo_restante:
            return "si"
        
        k += 1
    
    return "no"

def main():
    n = int(input())  
    resultados = []
    for _ in range(n):
        a, b = map(int, input().split())
        resultado = es_posible_cumplir_plazo(a, b)
        resultados.append(resultado)
    
    for res in resultados:
        print(res)

if __name__ == "__main__":
    main()