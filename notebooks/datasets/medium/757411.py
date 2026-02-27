def agregar(lista, valor):
    lista.append(valor)
    idx = len(lista) - 1
    while idx > 0:
        anterior = (idx - 1) // 2
        if lista[anterior] <= lista[idx]:
            break
        lista[idx], lista[anterior] = lista[anterior], lista[idx]
        idx = anterior

def extraer(lista):
    minimo = lista[0]
    lista[0] = lista[-1]
    lista.pop()
    idx = 0
    while True:
        izquierdo = 2 * idx + 1
        derecho = 2 * idx + 2
        menor = idx
        if izquierdo < len(lista) and lista[izquierdo] < lista[menor]:
            menor = izquierdo
        if derecho < len(lista) and lista[derecho] < lista[menor]:
            menor = derecho
        if menor == idx:
            break
        lista[idx], lista[menor] = lista[menor], lista[idx]
        idx = menor
    return minimo

while True:
    n = int(input())
    if n <= 0:
        break
    
    elementos = list(map(int, input().split()))
    monton = []
    for e in elementos:
        agregar(monton, e)
    
    suma_total = 0
    while len(monton) > 1:
        parcial = extraer(monton)
        parcial += extraer(monton)
        suma_total += parcial
        agregar(monton, parcial)
    
    print(suma_total)
