def solution(A, B):
    A_ = list(A)
    B_ = list(B)
    count = 0
    while A_ != B_:
        count += 1
        tmp = A_[-1]
        for i in range(len(A_)-1, 0, -1):
            A_[i] = A_[i-1]
        A_[0] = tmp
        print(A_)
        if count > len(A_):
            return -1
    return count