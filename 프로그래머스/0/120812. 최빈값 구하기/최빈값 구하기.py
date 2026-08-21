def solution(array):
    dit = dict()
    for a in array:
        dit[a] = dit.get(a, 0) + 1
    answer = array[0]
    v = []
    for key, value in dit.items():
        v.append(value)
        if dit[answer] < value:
            answer = key
    if v.count(dit[answer]) > 1:
        return -1
    return answer