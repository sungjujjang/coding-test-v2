from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    quque = deque([(0, 0, 1)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while quque:
        x, y, k = quque.popleft()

        if x == m - 1 and y == n - 1:
            return k

        for dx, dy in dirs:
            dx, dy = x + dx, y + dy

            if (0 <= dx < m) and (0 <= dy < n):
                if maps[dy][dx] == 1 and not visited[dy][dx]:
                    visited[dy][dx] = True
                    quque.append((dx, dy, k+1))

    return -1