def solution(bin1, bin2):
    n = int(bin1, 2) + int(bin2, 2)
    return format(n, 'b')