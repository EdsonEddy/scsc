from collections import deque
direcs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
 
def lugaresV(x, y, ciudad):
    
    cola = deque()
    cola.append((X, Y))
    lugares = 0  
    while cola:
        x1, y1 = cola.popleft()
        lugares += 1
 
        ciudad[x1][y1] = '#'  
 
        for dx, dy in direcs:
            x2, y2 = x1 + dx, y1 + dy
            if 0 <= x2 < x and 0 <= y2 < y and ciudad[x2][y2] == '.':
                cola.append((x2, y2))
                ciudad[x2][y2] = '#'  
    return lugares
 
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    ciudad = [list(input()) for _ in range(x)]
    for i in range(x):
        for j in range(y):
            if ciudad[i][j] == '@':
                X, Y = i, j
                break
    print(lugaresV(x, y, ciudad))