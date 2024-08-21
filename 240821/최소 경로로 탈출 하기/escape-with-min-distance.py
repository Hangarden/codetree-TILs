# n, m 입력
n, m = map(int, input().split())
# maze 입력
maze = [
    list(map(int, input().split()))
    for _ in range(n)
]

# in_range(x, y)
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# can_go(x, y)
def can_go(x, y):
    # 범위 내에 있고, 방문한 적 없으며, 1이면 가능
    return in_range(x, y) and not visited[x][y] and maze[x][y]

# bfs()
def bfs():
    while q:
        x, y = q.popleft()
        dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            # 갈 수 있으면
            if can_go(nx, ny):
                # 방문 처리 후
                visited[nx][ny] = True
                # step 처리 후
                step[nx][ny] = step[x][y] + 1
                # 큐에 넣어주기
                q.append((nx, ny))

# 설계
# visited
visited = [
    [False] * m
    for _ in range(n)
]

# step
step = [
    [0] * m
    for _ in range(n)
]

# 큐 사용준비
from collections import deque
q = deque()


# 큐에 넣어주고
q.append((0, 0))
# 방문 처리 후
visited[0][0] = True
# bfs()
bfs()

# 방문했으면
if visited[-1][-1]:
    # 거리 출력
    print(step[-1][-1])
# 방문 못했으면
else:
    # -1 출력
    print(-1)