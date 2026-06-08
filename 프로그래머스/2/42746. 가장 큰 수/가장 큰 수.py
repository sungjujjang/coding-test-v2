def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    stri = "".join(numbers)
    if stri == "0"*len(stri):
        return "0"
    return stri