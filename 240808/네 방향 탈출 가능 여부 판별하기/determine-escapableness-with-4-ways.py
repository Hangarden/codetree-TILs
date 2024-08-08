from collections import deque

def is_path_possible(n, m, grid):
    # Directions for movement: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Start BFS from the top-left corner
    queue = deque([(0, 0)])
    visited = set()
    visited.add((0, 0))
    
    # Since the problem states the start and end are not blocked, we skip initial checks

    while queue:
        x, y = queue.popleft()
        
        # If we reach the bottom-right corner
        if (x, y) == (n-1, m-1):
            return 1
        
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and grid[nx][ny] == 1:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    # If no path found
    return 0

# Example usage:
n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

result = is_path_possible(n, m, grid)
print(result)  # Output should match the expected result for given examples