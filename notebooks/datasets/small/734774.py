import sys
sys.setrecursionlimit(10000)  


def dfs(x, y, city, visited, rows, cols):
    if x < 0 or y < 0 or x >= rows or y >= cols or city[x][y] == '#' or visited[x][y]:
        return 0
    
    visited[x][y] = True
    
    count = 1
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        count += dfs(x + dx, y + dy, city, visited, rows, cols)
    return count

def main():
    while True:
        
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            break
        
        city = [list(input().strip()) for _ in range(x)]
        
        start_x, start_y = -1, -1
        for i in range(x):
            for j in range(y):
                if city[i][j] == '@':
                    start_x, start_y = i, j
                    break
            if start_x != -1:
                break
        
        
        visited = [[False] * y for _ in range(x)]
        
        
        result = dfs(start_x, start_y, city, visited, x, y)
        print(result)

if __name__ == "__main__":
    main()
