def solution(quiz):
    answer = []
    for q in quiz:
        ql = q.split()
        a = int(ql[0])
        attr = ql[1]
        b = int(ql[2])
        rst = int(ql[4])
        if attr == "+":
            if a+b == rst:
                answer.append("O")
            else:
                answer.append("X")
        else:
            if a-b == rst:
                answer.append("O")
            else:
                answer.append("X")
    return answer