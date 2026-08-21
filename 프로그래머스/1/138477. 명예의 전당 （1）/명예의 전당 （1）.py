import heapq

def solution(k, score):
    hp = []
    answer = []
    for i in range(k if k <= len(score) else len(score)):
        new_hp = []
        heapq.heappush(hp, -1 * score[i])
        for j in range(len(hp)):
            new_hp.append(heapq.heappop(hp))
        answer.append(-1 * new_hp[-1])
        heapq.heapify(new_hp)
        hp = new_hp
    for i in range(k, len(score)):
        new_hp = []
        heapq.heappush(hp, -1 * score[i])
        for j in range(k):
            new_hp.append(heapq.heappop(hp))
        answer.append(-1 * new_hp[-1])
        heapq.heapify(new_hp)
        hp = new_hp
    return answer