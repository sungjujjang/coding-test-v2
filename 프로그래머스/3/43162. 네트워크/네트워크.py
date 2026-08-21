from collections import deque

def solution(n, computers):
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                graph[i].append(j)
    visited = [0] * n
    visit = 1
    while True:
        if 0 not in visited:
            break
        start = visited.index(0)
        q = deque([start])
        while q:
            temp = q.popleft()
            visited[temp] = visit
            for i in graph[temp]:
                if visited[i] == 0:
                    q.append(i)
        visit += 1
    answer = 0
    return visit-1