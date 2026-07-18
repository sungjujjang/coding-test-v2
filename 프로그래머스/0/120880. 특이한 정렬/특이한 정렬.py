def solution(numlist, n):
    new_numlist = [[abs(n-i), i] for i in numlist]
    new_numlist.sort(key= lambda x: (x[0], -x[1]))
    answer = list(map(lambda x: x[1], new_numlist))
    return answer