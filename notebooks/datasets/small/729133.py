from collections import deque
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
 
def lugares_visitables(x, y, ciudad):
    
    cola = deque()
    cola.append((x_inicio, y_inicio))
    lugares = 0  
    while cola:
        x_actual, y_actual = cola.popleft()
        lugares += 1
 
        ciudad[x_actual][y_actual] = '#'  
 
        for dx, dy in directions:
            x_nuevo, y_nuevo = x_actual + dx, y_actual + dy
            if 0 <= x_nuevo < x and 0 <= y_nuevo < y and ciudad[x_nuevo][y_nuevo] == '.':
                cola.append((x_nuevo, y_nuevo))
                ciudad[x_nuevo][y_nuevo] = '#'  
    return lugares
 
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    ciudad = [list(input()) for _ in range(x)]
    for i in range(x):
        for j in range(y):
            if ciudad[i][j] == '@':
                x_inicio, y_inicio = i, j
                break
    print(lugares_visitables(x, y, ciudad))