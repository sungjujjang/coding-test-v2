from collections import deque

def solution(progresses, speeds):
    qeque = deque(progresses)
    speed_ = deque(speeds)
    answer = []
    while qeque:
        cnt = 0
        while qeque and qeque[0] >= 100:
            qeque.popleft()
            speed_.popleft()
            cnt += 1
        if cnt:
            answer.append(cnt)
        for i in range(len(qeque)):
            qeque[i] += speed_[i]
    return answer