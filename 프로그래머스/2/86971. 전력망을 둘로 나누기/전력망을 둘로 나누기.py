from collections import deque

def without(wires, wire):
    result = []
    for w in wires:
        if w != wire:
            result.append(w)
    return result

def solution(n, wires):
    answer = []
    for wire in wires:
        new = without(wires, wire)
        visited = [0] * (n+1)
        visited[0] = 9
        graph = [[] for i in range(n+1)]
        for a, b in new:
            graph[a].append(b)
            graph[b].append(a)
        quque = deque([1])
        while quque:
            now = quque.popleft()
            visited[now] = 1
            for i in graph[now]:
                if visited[i] == 0:
                    quque.append(i)
        if 0 in visited:
            quque = deque([visited.index(0)])
            while quque:
                now = quque.popleft()
                visited[now] = 2
                for i in graph[now]:
                    if visited[i] != 2:
                        quque.append(i)
        answer.append(abs(visited.count(1)-visited.count(2)))
    return min(answer)