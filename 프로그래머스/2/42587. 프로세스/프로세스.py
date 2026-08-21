from collections import deque

def solution(priorities, location):
    qeque = deque()
    for i in range(len(priorities)):
        qeque.append((i, priorities[i]))
    tmp = (-1, -1)
    answer = 0
    while True:
        tmp = qeque.popleft()
        chk = True
        for q in qeque:
            if q[1] > tmp[1]:
                qeque.append(tmp)
                chk = False
                break
        if chk:
            answer += 1
            if tmp[0] == location:
                break
    return answer