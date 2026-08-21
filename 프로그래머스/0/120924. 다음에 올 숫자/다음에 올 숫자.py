def solution(common):
    gap1 = common[0] - common[1]
    gap2 = common[1] - common[2]
    if gap1 == gap2:
        answer = common[-1] - gap1
    else:
        answer = common[-1] * (common[1]/common[0])
    return answer