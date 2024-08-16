dx = [0, -1, 0, 1]  # 오른쪽, 위, 왼쪽, 아래
dy = [1, 0, -1, 0]

memo = {}

def throw(i, j, direction):
    if (i, j, direction) in memo:
        return memo[(i, j, direction)]

    count = 0
    x, y = i, j

    while 0 <= x < n and 0 <= y < n:
        x += dx[direction]
        y += dy[direction]
        count += 1

        if not (0 <= x < n and 0 <= y < n):
            memo[(i, j, direction)] = count
            return count

        if maps[x][y] == 1:
            direction = (direction + 1) % 4 if direction % 2 == 0 else (direction - 1) % 4
        elif maps[x][y] == 2:
            direction = (direction - 1) % 4 if direction % 2 == 0 else (direction + 1) % 4
    
    memo[(i, j, direction)] = count
    return count

def find_max_time():
    max_time = 0
    
    # 상단, 하단, 좌측, 우측의 모든 시작점에 대해 계산
    for start in range(4 * n):
        if start < n:  # 상단에서 시작
            i, j, direction = 0, start, 1
        elif start < 2 * n:  # 우측에서 시작
            i, j, direction = start - n, n - 1, 2
        elif start < 3 * n:  # 하단에서 시작
            i, j, direction = n - 1, n - 1 - (start - 2 * n), 3
        else:  # 좌측에서 시작
            i, j, direction = n - 1 - (start - 3 * n), 0, 0
        
        max_time = max(max_time, throw(i, j, direction))
    
    return max_time

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

print(find_max_time())