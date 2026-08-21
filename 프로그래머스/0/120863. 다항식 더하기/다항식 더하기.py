def solution(polynomial):
    pl = polynomial.split("+")
    x = 0
    integer = 0
    for p in pl:
        tmp = p.strip()
        if 'x' == tmp:
            x += 1
        elif 'x' in tmp:
            x += int(tmp.split("x")[0])
        else:
            integer += int(tmp)
    answer = []
    if x == 1:
        answer.append("x")
    elif x > 0:
        answer.append(str(x)+"x")
    if integer > 0:
        answer.append(str(integer))
    return " + ".join(answer)