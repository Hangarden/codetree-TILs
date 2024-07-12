import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
# print(graph)
for i in range(N+1):
    graph[i].sort()

def DFS(v, visited):
    print(v, end= " ")
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i, visited)

def BFS(v, visited):
    q = deque()
    visited[v] = True
    q.append(v)

    while q:
        x = q.popleft()
        print(x, end=" ")

        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

visited1 = [False for _ in range(N+1)]
visited2 = [False for _ in range(N+1)]

# print(visited)
DFS(V, visited1)
print()
BFS(V, visited2)
# print(graph)
