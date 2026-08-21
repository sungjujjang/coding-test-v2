from collections import deque

def solution(numbers, target):
    max_idx = len(numbers) - 1
    q = deque([(0, numbers[0]), (0, -numbers[0])])
    answer = 0
    
    while q:
        idx, total = q.pop()
        
        if idx == max_idx:
            if total == target:
                answer += 1
            continue
            
        idx += 1
        q.append((idx, total + numbers[idx]))
        q.append((idx, total - numbers[idx]))
        
    return answer