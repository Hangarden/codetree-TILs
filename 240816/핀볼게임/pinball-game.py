dx = [0, -1, 0, 1]  # 오른쪽, 위, 왼쪽, 아래
dy = [1, 0, -1, 0]

memo = {}  # 메모이제이션을 위한 딕셔너리

def check(i,j):
    if j==0 and 0< i < n-1: # 왼쪽 -> 오른쪽
        return [0]
    if i==0 and 0< j < n-1:
        return [3]
    if i==n-1 and 0< j < n-1:
        return [1]
    if j==n-1 and 0 < i < n-1:
        return [2]

    if i == 0 and j == 0:
        return [0,3]
    if i == (n-1) and j == 0:
        return [0,1]
    if i ==0 and j == (n-1):
        return [2,3]
    if i ==(n-1) and j == (n-1):
        return [1,2]
    
def throw(i, j, direction):
    if (i, j, direction) in memo:  # 이미 계산된 경우
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
            direction = abs(direction - 5) % 4  # 기존 수식 사용

        if maps[x][y] == 2:
            direction = abs(direction - 3) % 4  # 기존 수식 사용

    memo[(i, j, direction)] = count
    return count


n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

nums1 = [0, n - 1]
max_val = -888

for i in nums1:  # 상단과 하단 (i가 0 또는 n-1인 경우)
    for j in nums1:  # 좌측과 우측 (j가 0 또는 n-1인 경우)
        direction = check(i, j)
        if len(direction) >= 2:
            max_val = max(max_val, throw(i, j, direction[0]))
            max_val = max(max_val, throw(i, j, direction[1]))

for i in nums1:  # 상단과 하단
    for j in range(1, n - 1):  # 가운데 열들
        direction = check(i, j)
        if len(direction) == 1:
            max_val = max(max_val, throw(i, j, direction[0]))

for i in range(1, n - 1):  # 가운데 행들
    for j in nums1:  # 좌측과 우측
        direction = check(i, j)
        if len(direction) == 1:
            max_val = max(max_val, throw(i, j, direction[0]))

print(max_val + 1)