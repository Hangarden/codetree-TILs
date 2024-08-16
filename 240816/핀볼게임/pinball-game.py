dx = [0, -1, 0, 1]  # 오른쪽, 위, 왼쪽, 아래
dy = [1, 0, -1, 0]

def throw(i, j, direction):
    count = 0
    visited = set()  # 방문한 위치와 방향을 저장

    while 0 <= i < n and 0 <= j < n:
        if (i, j, direction) in visited:  # 이미 같은 위치와 방향을 방문했다면 무한 루프
            return float('inf')  # 무한루프를 나타내는 큰 값을 반환
        visited.add((i, j, direction))

        i += dx[direction]
        j += dy[direction]
        count += 1

        if not (0 <= i < n and 0 <= j < n):
            return count

        if maps[i][j] == 1:
            direction = abs(direction - 5) % 4
        
        if maps[i][j] == 2:
            direction = abs(direction - 3) % 4

    return count

def check(i,j):
    if j==0 and 0< i < n-1:  # 왼쪽 -> 오른쪽
        return [0]
    if i==0 and 0< j < n-1:  # 위쪽 -> 아래쪽
        return [3]
    if i==n-1 and 0< j < n-1:  # 아래쪽 -> 위쪽
        return [1]
    if j==n-1 and 0 < i < n-1:  # 오른쪽 -> 왼쪽
        return [2]

    if i == 0 and j == 0:
        return [0, 3]
    if i == (n-1) and j == 0:
        return [0, 1]
    if i == 0 and j == (n-1):
        return [2, 3]
    if i == (n-1) and j == (n-1):
        return [1, 2]

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

nums1 = [0, n-1]
max_val = 1

for i in nums1:  # 상단과 하단
    for j in nums1:  # 좌측과 우측
        direction = check(i, j)
        if len(direction) >= 2:
            result1 = throw(i, j, direction[0])
            if result1 != float('inf'):
                max_val = max(max_val, result1)
            result2 = throw(i, j, direction[1])
            if result2 != float('inf'):
                max_val = max(max_val, result2)

for i in nums1:  # 상단과 하단
    for j in range(1, n-1):  # 가운데 열들
        direction = check(i, j)
        if len(direction) == 1:
            result = throw(i, j, direction[0])
            if result != float('inf'):
                max_val = max(max_val, result)

for i in range(1, n-1):  # 가운데 행들
    for j in nums1:  # 좌측과 우측
        direction = check(i, j)
        if len(direction) == 1:
            result = throw(i, j, direction[0])
            if result != float('inf'):
                max_val = max(max_val, result)

print(max_val + 1)