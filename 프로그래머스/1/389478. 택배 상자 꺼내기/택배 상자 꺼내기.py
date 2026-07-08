import math

def solution(n, w, num):
    li = []
    
    i = -1
    for i in range(0, n//w):
        if i % 2 == 0:
            li.append(list(range(w*i+1, w*i+w+1)))
        else:
            li.append(list(range(w*i+w, w*i, -1)))
    if n%w != 0:
        i += 1
        if i % 2 == 0:
            li.append(list(range(w*i+1, n+1)) + [0] * (w-(n-(w*i+1)+1)))
        else:
            li.append( [0] * (w-(n-(w*i+1)+1))+ list(range(n, w*i, -1)))
    
    ans = 0
    idx = -1
    
    li.reverse()
    
    while li:
        tmp = li.pop()
        if idx == -1:
            try:
                idx_ = tmp.index(num)
            except ValueError:
                continue
            idx = idx_
            ans += 1
        else:
            if tmp[idx] != 0:
                ans += 1
    return ans