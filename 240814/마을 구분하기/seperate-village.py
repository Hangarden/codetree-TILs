n = int(input())
vill = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[False]*n for _ in range(n)]

dxs = [0, +1, 0, -1]
dys = [-1, 0, +1, 0]

people_num = 0
people_nums = []

def can_go(x, y):
    if x >= 0 and x < n and y >= 0 and y < n:
        if not visited[x][y] and vill[x][y] != 0:
            return True
    return False

def dfs(x, y):
    global people_num
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if can_go(nx, ny):
            visited[nx][ny] = True
            people_num += 1

            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            visited[i][j] = True
            people_num = 1
            dfs(i, j) 
            people_nums.append(people_num)

people_nums = sorted(people_nums)

print(len(people_nums))
for p in people_nums:
    print(p)