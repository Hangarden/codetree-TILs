def explode_and_apply_gravity(grid, n, x, y):
    # 폭발 크기
    size = grid[x][y]
    # 폭발 영역
    explosion_zone = [[False] * n for _ in range(n)]
    
    # 폭발 처리
    explosion_zone[x][y] = True  # 중심 폭발
    for dx in range(1, size):
        # 위쪽
        if x - dx >= 0:
            explosion_zone[x - dx][y] = True
        # 아래쪽
        if x + dx < n:
            explosion_zone[x + dx][y] = True
        # 왼쪽
        if y - dx >= 0:
            explosion_zone[x][y - dx] = True
        # 오른쪽
        if y + dx < n:
            explosion_zone[x][y + dx] = True
    
    # 폭발 반영
    new_grid = [[grid[i][j] if not explosion_zone[i][j] else 0 for j in range(n)] for i in range(n)]
    
    # 중력 작용
    for col in range(n):
        # 각 열마다 0이 아닌 숫자를 아래로 내리기 위한 스택을 사용
        stack = []
        for row in range(n):
            if new_grid[row][col] != 0:
                stack.append(new_grid[row][col])
        
        # 맨 아래부터 다시 숫자를 채워 넣기
        for row in range(n - 1, -1, -1):
            if stack:
                new_grid[row][col] = stack.pop()
            else:
                new_grid[row][col] = 0
    
    return new_grid

def count_pairs(grid, n):
    count = 0
    for i in range(n):
        for j in range(n):
            # 오른쪽 확인
            if j + 1 < n and grid[i][j] == grid[i][j + 1]:
                count += 1
            # 아래쪽 확인
            if i + 1 < n and grid[i][j] == grid[i + 1][j]:
                count += 1
    return count

def find_best_explosion(grid, n):
    max_pairs = 0
    for i in range(n):
        for j in range(n):
            # 각 위치에서 폭발 후 결과를 계산
            new_grid = explode_and_apply_gravity(grid, n, i, j)
            pairs = count_pairs(new_grid, n)
            max_pairs = max(max_pairs, pairs)
    return max_pairs

# 입력
n = int(input().strip())
grid = [list(map(int, input().strip().split())) for _ in range(n)]

# 최적의 폭발 위치 찾기
result = find_best_explosion(grid, n)
print(int(result/2))