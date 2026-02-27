def procesar_numero(n):
    original = n
    pasos = []
    while n > 81:
        ult_digito = n % 10
        resto = n // 10
        pasos.append((resto, ult_digito))
        n = resto + ult_digito * 5
    resultado = n
    estado = "correcto" if resultado % 7 == original % 7 else "incorrecto"
    salida = ''.join(f"({a}, {b})" for a, b in pasos)
    return f"{salida} {resultado} {estado}"

def main():
    t = int(input())
    for _ in range(t):
        numero = int(input())
        print(procesar_numero(numero))

if __name__ == "__main__":
    main()
