def solution(a, b, c, d):
    arr = [a, b, c, d]
    arr.sort()
    if a == b == c == d:
        answer = a*1111
    elif arr[0] == arr[1] == arr[2]:
        answer = (10 * arr[0] + arr[3])**2
    elif arr[1] == arr[2] == arr[3]:
        answer = (10 * arr[1] + arr[0])**2
    elif arr[0] == arr[1] and arr[2] == arr[3]:
        answer = (arr[0] + arr[2]) * abs(arr[0] - arr[2])
    elif arr[0] == arr[1]:
        answer = arr[2] * arr[3]
    elif arr[1] == arr[2]:
        answer = arr[0] * arr[3]
    elif arr[2] == arr[3]:
        answer = arr[0] * arr[1]
    else:
        answer = arr[0]
    return answer
