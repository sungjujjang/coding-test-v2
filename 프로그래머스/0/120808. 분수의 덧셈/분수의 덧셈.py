import math

def solution(numer1, denom1, numer2, denom2):
    upp = numer1 * denom2 + numer2 * denom1
    don = denom1 * denom2
    l = math.gcd(upp, don)
    answer = [upp // l, don // l]
    return answer