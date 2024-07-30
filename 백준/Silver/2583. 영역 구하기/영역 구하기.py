from collections import deque

# 입력받기
M, N, K = map(int, input().split())
maps = [[0 for _ in range(N)] for _ in range(M)]

# 직사각형 영역 표시하기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            maps[i][j] = 1

# 유효한 좌표인지 확인하는 함수
def valid(x, y):
    return 0 <= x < M and 0 <= y < N

# BFS를 이용하여 영역의 넓이를 구하는 함수
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    count = 0
    while q:
        cx, cy = q.popleft()
        count += 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if valid(nx, ny) and not visited[nx][ny] and maps[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))
    return count

visited = [[False for _ in range(N)] for _ in range(M)]
areas = []

# 모든 좌표를 확인하며 BFS 수행
for i in range(M):
    for j in range(N):
        if not visited[i][j] and maps[i][j] == 0:
            areas.append(bfs(i, j))

# 결과 출력
areas.sort()
print(len(areas))
print(" ".join(map(str, areas)))
