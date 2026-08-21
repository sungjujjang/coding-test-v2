from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
    ran = [0] * (n+1)
    quque = deque([(1, 1)])
    visited[1] = True
    while quque:
        tmp = quque.popleft()
        node, _range = tmp
        ran[_range] += 1
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                quque.append((i, _range+1))
    ran[0] = 1
    idx = ran.index(0)
    return ran[idx-1]