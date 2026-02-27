def calcular(n):
    return int(n * 100 + 0.5) / 100
def calcular_porcentaje_de_frutas(n):
    vo = 'aeiou'
    t = len(n)
    dic = {}
    for fruta in vo:
        cont = n.count(fruta)
        p = (cont * 100) / t
        dic[fruta] = calcular(p)
 
    return dic
def procesar_casos_de_prueba(n):
    for caso in n:
        r = calcular_porcentaje_de_frutas(caso)
        for fruta, por in r.items():
            print(f"{fruta}= {por:.2f}")
 
if __name__ == "__main__":
    T = int(input())
    v = []
    for _ in range(1,T+1,1):
        n = input()
        v.append(n)
        print(f'Caso {_}:')
        procesar_casos_de_prueba(v)
        v=[]
 