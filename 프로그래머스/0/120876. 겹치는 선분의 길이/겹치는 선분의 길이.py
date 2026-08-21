def solution(lines):
    cnt = [0] * 201

    for s, e in lines:
        for i in range(s + 100, e + 100):
            cnt[i] += 1

    return sum(1 for x in cnt if x >= 2)