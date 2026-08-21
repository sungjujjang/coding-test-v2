def solution(chicken):
    answer = 0
    now = chicken
    while now >= 10:
        tmp = now // 10
        answer += tmp
        now = (now % 10) + tmp
    return answer