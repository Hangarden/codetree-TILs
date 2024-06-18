import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

dx = [1,-1,0,0,   1,1,-1,-1]
dy = [0, 0,-1,1,  1,-1,1,-1]

def dfs(x,y):
    visited[x][y] = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < height and 0 <= ny < width and not visited[nx][ny] and maps[nx][ny] == 1:
            dfs(nx,ny)

    return



while True:

    width, height = map(int, input().split())

    if width == height == 0:
        break

    maps = []

    visited = [ [False for _ in range(width)] for _ in range(height) ]
    for _ in range(height):
        maps.append(list(map(int, input().split())))
    cnt = 0
    for x in range(height):
        for y in range(width):
            if maps[x][y] == 1 and visited[x][y] == False:
                dfs(x,y)
                cnt += 1

    print(cnt)


