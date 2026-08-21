def solution(answers):
    l = len(answers)
    one = [1, 2, 3, 4, 5] * l
    two = [2, 1, 2, 3, 2, 4, 2, 5] * l
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * l
    
    li = [0, 0, 0]
    for i in range(l):
        if answers[i] == one[i]:
            li[0] += 1
        if answers[i] == two[i]:
            li[1] += 1
        if answers[i] == thr[i]:
            li[2] += 1
    anss = max(li)
    answer = []
    for i in range(len(li)):
        if li[i] == anss:
            answer.append(i+1)
    return answer