vocales = 'aeiou'
def redondeo_java(value):
    if value >= 0:
        return int(value + 0.5)
    else:
        return int(value - 0.5)

def calcular_porcentajes(s,i):
    p = len(s)
    resultado = f"Caso {i+1}:"
    for v in vocales:
        cant = s.count(v)
        #print(f"{v} = {cant}")
        if p > 0:
            porcentaje = ((cant / p) * 100)
        else:
            porcentaje = 0
        porcentaje_redondeado = redondeo_java(porcentaje * 100) / 100
        #print(f"{porcentaje_redondeado}")
        resultado += f"\n{v}= {porcentaje_redondeado:.2f}"
    return resultado

# Entrada de datos
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        caso=input().strip()
        result=calcular_porcentajes(caso,i)
        print(result)