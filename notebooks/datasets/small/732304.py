def contar_lugares(city, start_x, start_y):
    x_len = len(city)
    y_len = len(city[0]) if x_len > 0 else 0
    visited = [[False] * y_len for _ in range(x_len)]
    stack = [(start_x, start_y)]
    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while stack:
        current_x, current_y = stack.pop()
        if visited[current_x][current_y]:
            continue 
        visited[current_x][current_y] = True
        count += 1 
        for dx, dy in directions:
            new_x, new_y = current_x + dx, current_y + dy
            if 0 <= new_x < x_len and 0 <= new_y < y_len and not visited[new_x][new_y] and city[new_x][new_y] != '#':
                stack.append((new_x, new_y))
    return count
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    city = [input().strip() for _ in range(x)]
    start_x = start_y = -1
    for i in range(x):
        for j in range(y):
            if city[i][j] == '@':
                start_x, start_y = i, j
                break
        if start_x != -1:
            break
    resultado = contar_lugares(city, start_x, start_y)
    print(resultado)