def solution(num, total):
    t = list(range(1, num+1))
    x = (total - sum(t))//num
    answer = list(map(lambda u: u+x, t))
    return answer