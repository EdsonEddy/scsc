t = int(input())
for _ in range(t):
    numero_original = int(input())
    resto_original = numero_original % 7
    pasos = []
    numero_actual = numero_original
    while numero_actual > 81:
        ultimo_digito = numero_actual % 10
        resto_digitos = numero_actual // 10
        pasos.append((resto_digitos, ultimo_digito))
        numero_actual = resto_digitos + (ultimo_digito * 5)
    resto_final = numero_actual % 7
    resultado = ""
    for par in pasos:
        resultado += f"({par[0]}, {par[1]})"
    if resto_final == resto_original:
        resultado += f" {numero_actual} correcto"
    else:
        resultado += f" {numero_actual} incorrecto"
    
    print(resultado)