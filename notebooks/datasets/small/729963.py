def dfs(mapa, x, y, visitado):
    if x < 0 or x >= len(mapa) or y < 0 or y >= len(mapa[0]) or (mapa[x][y] != '.' and mapa[x][y] != '@') or visitado[x][y]:
        return 0
    visitado[x][y] = True
    count = 1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        count += dfs(mapa, x + dx, y + dy, visitado)
    return count

def main():
    while True:
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            break
        
        mapa = [input().strip() for _ in range(x)]
        visitado = [[False] * y for _ in range(x)]
        pos_inicial = next((i, j) for i in range(x) for j in range(y) if mapa[i][j] == '@')
        
        total_lugares = dfs(mapa, pos_inicial[0], pos_inicial[1], visitado)
        print(total_lugares)

if __name__ == "__main__":
    main()
