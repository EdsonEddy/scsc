def dfs(matrix, x, y, visited):
    if (x, y) in visited:
        return 0
    visited.add((x, y))
    count = 1  
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] in ('.', '@'):
            count += dfs(matrix, nx, ny, visited)
    return count
def main():
    while True:
        x, y = map(int, input().strip().split())
        if x == 0 and y == 0:
            break
        matrix = [input().strip() for _ in range(x)]
        visited = set()        
        start_x = start_y = -1
        for i in range(x):
            for j in range(y):
                if matrix[i][j] == '@':
                    start_x, start_y = i, j
                    break
            if start_x != -1:
                break        
        result = dfs(matrix, start_x, start_y, visited)
        print(result)
if __name__ == "__main__":
    main()
