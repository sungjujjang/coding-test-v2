answer = []

def hanoi(n, start, tmp, end):
    if n <= 1:
        answer.append([start, end])
        return
    hanoi(n-1, start, end, tmp)
    answer.append([start, end])
    hanoi(n-1, tmp, start, end)
    

def solution(n):
    hanoi(n, 1, 2, 3)
    return answer