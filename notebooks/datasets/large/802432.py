import sys
from decimal import Decimal, ROUND_HALF_UP, getcontext
getcontext().prec = 60

def resolver():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    
    for i in range(1, t + 1):
        s = input_data[i]
        total_cultivos = len(s)
        print(f"Caso {i}:")

        frutas = ['a', 'e', 'i', 'o', 'u']
        
        for fruta in frutas:
            cantidad = s.count(fruta)
            porcentaje = (Decimal(cantidad) * Decimal(100)) / Decimal(total_cultivos)
            resultado_final = porcentaje.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
            print(f"{fruta}= {resultado_final}")

if __name__ == "__main__":
    resolver()