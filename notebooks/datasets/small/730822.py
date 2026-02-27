def count_reachable_places(grid, rows, cols):
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def find_start():
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '@':
                    return i, j
        return -1, -1
    
    def dfs(x, y, visited):
        if not is_valid(x, y) or grid[x][y] == '#' or (x, y) in visited:
            return 0
        
        count = 1 
        visited.add((x, y))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            count += dfs(new_x, new_y, visited)
            
        return count
    
    start_x, start_y = find_start()
    if start_x == -1:  
        return 0
    
    return dfs(start_x, start_y, set())

def main():
    while True:
        rows, cols = map(int, input().split())
        
        if rows == 0 and cols == 0:
            break
            
        grid = []
        for _ in range(rows):
            grid.append(list(input().strip()))
            
        result = count_reachable_places(grid, rows, cols)
        print(result)

if __name__ == "__main__":
    main()