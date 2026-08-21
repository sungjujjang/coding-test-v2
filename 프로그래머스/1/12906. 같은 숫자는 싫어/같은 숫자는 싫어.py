from collections import deque

def solution(arr):
    arr_queue = deque(arr)
    last = -1
    answer = []
    while arr_queue:
        tmp = arr_queue.popleft()
        if last != tmp:
            answer.append(tmp)
            last = tmp
    return answer