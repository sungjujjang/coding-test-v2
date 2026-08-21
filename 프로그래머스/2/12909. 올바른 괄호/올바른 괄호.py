from collections import deque

def solution(s):
    answer = True
    arr = list(s)
    stack = deque()
    for c in arr:
        if c == "(":
            stack.append(c)
        else:
            if not stack:
                return False
            stack.popleft()
    if stack:
        return False
    return True