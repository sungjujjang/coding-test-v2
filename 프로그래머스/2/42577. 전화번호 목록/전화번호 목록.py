def solution(phone_book):
    answer = True
    book = set(phone_book)
    for phone in phone_book:
        for i in range(len(phone)):
            pre = phone[:i]
            
            if pre in book:
                return False
    return answer