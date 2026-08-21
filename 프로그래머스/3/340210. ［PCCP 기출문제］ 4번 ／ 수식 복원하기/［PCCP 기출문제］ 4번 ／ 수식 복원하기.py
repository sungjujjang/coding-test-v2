def change(a, n):
    if a == 0: return "0"
    ans = []
    while a != 0:
        ans.append(str(a % n))
        a //= n
    return "".join(reversed(ans))

def solution(expressions):
    problems = []
    knowns = []
    max_digit = 0
    
    for exp in expressions:
        parts = exp.split()
        for p in [parts[0], parts[2], parts[4]]:
            if p != "X":
                for char in p:
                    max_digit = max(max_digit, int(char))
        
        if parts[4] == "X":
            problems.append(parts)
        else:
            knowns.append(parts)

    candidates = set(range(max(2, max_digit + 1), 10))
    
    for ex in knowns:
        temp_candidates = set()
        for base in candidates:
            num1 = int(ex[0], base)
            num2 = int(ex[2], base)
            result = int(ex[4], base)
            
            if ex[1] == '+':
                if num1 + num2 == result:
                    temp_candidates.add(base)
            else: # '-' 인 경우
                if num1 - num2 == result:
                    temp_candidates.add(base)
        candidates &= temp_candidates

    answer = []
    for pr in problems:
        results = set()
        for base in candidates:
            n1 = int(pr[0], base)
            n2 = int(pr[2], base)
            res = n1 + n2 if pr[1] == '+' else n1 - n2
            results.add(change(res, base))
        
        if len(results) == 1:
            res_str = list(results)[0]
            answer.append(f"{pr[0]} {pr[1]} {pr[2]} = {res_str}")
        else:
            answer.append(f"{pr[0]} {pr[1]} {pr[2]} = ?")
            
    return answer