import copy
import itertools
from collections import deque

n, m = map(int, input().split())

lab = []

for _ in range(n):
    lst = list(map(int, input().split()))
    lab.append(lst)

# print(lab)
wall = []
empty = []
virus = []
for i in range(n):
    for j in range(m):
        if lab[i][j]== 0:
          empty.append((i,j))
        elif lab[i][j]== 1:
          wall.append((i,j))
        else:
            virus.append((i,j))
make_wall = itertools.combinations(empty, 3)
dx, dy = [1,-1,0,0],[0,0,1,-1]
def spread_virus(lab_map, virus):
    q = deque(virus)

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and lab_map[nx][ny] == 0:
                lab_map[nx][ny] = 1
                q.append((nx, ny))


    return lab_map
max_count = -1
for i in make_wall:
    # 벽 셋팅
    lab2 = copy.deepcopy(lab)
    lab2[i[0][0]][i[0][1]] = 1
    lab2[i[1][0]][i[1][1]] = 1
    lab2[i[2][0]][i[2][1]] = 1
    # 바이러스 전파
    x = spread_virus(lab2, virus)
    count = 0
    for i in range(n):
        for j in range(m):
            if x[i][j] == 0:
                count += 1
    max_count = max(count, max_count)

print(max_count)