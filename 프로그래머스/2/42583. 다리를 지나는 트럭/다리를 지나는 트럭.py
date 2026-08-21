from collections import deque

def shift(li, checker):
    c = None
    for i in checker:
        if li[i] != 0:
            if i == 0:
                c = li[i]
                li[i] = 0
            else:
                li[i-1] = li[i]
                li[i] = 0
    return li, c

def count(li):
    cnt = 0
    for l in li:
        if l != 0:
            cnt += 1
    return cnt

def solution(bridge_length, weight, truck_weights):
    aller = len(truck_weights)
    on_bridge = [0] * bridge_length
    gone = []
    waiting = deque(truck_weights)
    answer = 0
    on_bridge_cnt = 0
    checker = []
    while waiting or sum(on_bridge):
        answer += 1
        on_bridge, c = shift(on_bridge, checker)
        new_checker = []
        for i in checker:
            if i-1 >= 0:
                new_checker.append(i-1)
        checker = new_checker
        if c:
            gone.append(c)
            on_bridge_cnt -= c
        if waiting:
            tmp = waiting[0]
            if on_bridge_cnt+tmp <= weight:
                on_bridge[-1] = waiting.popleft()
                checker.append(bridge_length-1)
                on_bridge_cnt += on_bridge[-1]
    return answer