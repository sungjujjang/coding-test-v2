from collections import deque

def solution(prices):
    answer = []
    for i, j in enumerate(prices):
        stack = deque()
        for z in range(i+1, len(prices)):
            stack.append(prices[z])
            if prices[i] > prices[z]:
                break
        answer.append(len(stack))
    return answer