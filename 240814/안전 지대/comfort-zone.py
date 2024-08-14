import sys
import heapq
sys.setrecursionlimit(2000) 


input = sys.stdin.readline

n, m = map(int, input().split(" "))

graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_val = 0
cnt = 0
answer = []
answer_k = -1
answer = -1

for _ in range(n):
    temp = list(map(int, input().strip().split()))
    graph.append(temp)
    max_val = max(max_val, max(temp))


def dfs(x, y, k):
    visited[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i] 

        if 0<=nx and nx <n and 0<=ny and ny <m:
            if not visited[nx][ny] and graph[nx][ny] > k:
                dfs(nx, ny, k)



for k in range(1, max_val+1):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] > k:
                dfs(i, j, k)
                cnt += 1

    if answer < cnt:
        answer = cnt
        answer_k = k


print(answer_k, answer)