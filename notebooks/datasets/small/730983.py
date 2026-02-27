  
def search(l, x, y, tuplas):
    
    mov = 0
    Y = [y-1, y+1, y, y]
    X = [x, x, x+1, x-1]
    for i in range(4):
        if 0<=X[i]<len(l[0]) and 0<=Y[i]<len(l):
            if not (X[i], Y[i]) in tuplas:
                if l[Y[i]][X[i]]=='.':
                    # print((X[i], Y[i]))
                    tuplas.append((X[i], Y[i]))
                    mov += 1 + search(l, X[i], Y[i], tuplas)
    return mov
# print(search(l1, 3, 5))

import sys

while True:

    columna, fila = map(int, sys.stdin.readline().strip().split())
    if fila == 0 and columna == 0:
        break
    
    l=[]
    for i in range(columna):
        linea = sys.stdin.readline().strip()
        tempL=[]
        for j in range(fila):
            tempL.append(linea[j])
            if linea[j]=='@':
                x=j
                y=i
        l.append(tempL)
    
    print(search(l, x, y, [])+1)