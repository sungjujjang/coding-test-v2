def solution(participant, completion):
    di = dict()
    for p in participant:
        di[p] = di.get(p, 0) + 1
    for c in completion:
        di[c] -= 1
    answer = ""
    for key, value in di.items():
        if value != 0:
            answer = key
    return answer