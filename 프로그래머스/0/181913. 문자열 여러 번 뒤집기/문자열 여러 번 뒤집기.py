def solution(my_string, queries):
    myli = list(my_string)
    for query in queries:
        newer = myli[query[0]:query[1]+1]
        newer.reverse()
        for i in range(query[0], query[1]+1):
            myli[i] = newer[i-query[0]]
    answer = "".join(myli)
    return answer