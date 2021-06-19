n, m = map(int,input().split())
graph = [[-1 for i in range(n)]for i in range(n)]
for i in range(m):
    u, v, w = map(int,input().split())
    graph[u][v] = graph[v][u] = w
A, B, K = map(int,input().split())
count = 0

def find(u, v, w, set = []):
    x = w
    global count
    if w > K:
        return 0
    set.append(v)
    for i in range(n):
        w = x
        if i not in set:
            if graph[v][i] != -1:
                if i == u:
                    w = w + graph[i][v]
                    if w == K:
                        count+=1
                else:
                    w = w + graph[i][v]
                    find(u, i, w)
    set.pop()

find(A, B, 0)
print(count)