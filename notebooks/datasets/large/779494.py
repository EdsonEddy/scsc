t = int(input())

for _ in range(t):
    n = input()
    original_mod = int(n) % 7
    pasos = []
    
    while True:
        if len(n) == 1:
            resultado = int(n)
            break
        parte_izquierda = n[:-1]
        ultimo_digito = int(n[-1])
        nuevo_valor = int(parte_izquierda) + ultimo_digito * 5
        pasos.append(f"({parte_izquierda}, {ultimo_digito})")
        n = str(nuevo_valor)
        if nuevo_valor <= 81:
            resultado = nuevo_valor
            break

    resultado_mod = resultado % 7
    veredicto = "correcto" if resultado_mod == original_mod else "incorrecto"
    print(''.join(pasos), resultado, veredicto)
