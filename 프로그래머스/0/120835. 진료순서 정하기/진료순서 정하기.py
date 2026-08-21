def solution(emergency):
    tmp = sorted(emergency)
    tmp.reverse()
    answer = []
    for i in emergency:
        answer.append(tmp.index(i)+1)
    return answer