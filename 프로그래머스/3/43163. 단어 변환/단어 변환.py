from collections import deque

def is_one_diff(a, b):
    diff = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    return diff == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    
    visited = [False] * len(words)
    
    q = deque([(begin, 0)])
    
    while q:
        word, step = q.pop()
        
        if word == target:
            return step
        
        step += 1
        
        for i in range(len(words)):
            if not visited[i]:
                if is_one_diff(word, words[i]):
                    visited[i] = True
                    q.append((words[i], step))
                    
    return 0