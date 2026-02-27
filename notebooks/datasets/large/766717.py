from decimal import Decimal, ROUND_HALF_UP

def main():
    t = int(input().strip())
    for i in range(t):
        dictionary = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        cadena = input().strip()
        total = len(cadena)
        for letra in cadena:
            if letra in dictionary:
                dictionary[letra] += 1
        print(f"Caso {i+1}:")
        for clave, valor in dictionary.items():
            porcentaje = (Decimal(valor) / Decimal(total) * 100) if total > 0 else Decimal("0.00")
            porcentaje_redondeado = porcentaje.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            print(f"{clave}= {porcentaje_redondeado}")

if __name__ == '__main__':
    main()
