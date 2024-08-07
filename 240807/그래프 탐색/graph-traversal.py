N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

visited = [ False for _ in range(N+1)]

# print(graph)
# print(visited)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

count = 0

def dfs(i):
    global count
    visited[i] = True
    count +=1
    for x in graph[i]:
        if not visited[x]:
            dfs(x)

dfs(1)

print(count-1)