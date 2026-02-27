def round_java_c_style(valor, decimales):
    factor = 10 ** decimales
    return int(valor * factor + 0.5) / factor
n=int(input())
for i in range(n):
    cad=input()
    vocales=dict()
    vocales["a"]=0
    vocales["e"]=0
    vocales["i"]=0
    vocales["o"]=0
    vocales["u"]=0
    print(f"Caso {i+1}:")
    for car in cad:
        if car in vocales:
            vocales[car]+=1
    tamanio=len(cad)
    for key in vocales:
        porcentaje=(vocales[key]/tamanio)*100
        porcentaje=round_java_c_style(porcentaje, 2)
        print(f"{key}= {porcentaje:.2f}")
    