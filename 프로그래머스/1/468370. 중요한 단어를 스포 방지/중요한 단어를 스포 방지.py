def check(spoiler_ranges, idx):
    for x, y in spoiler_ranges:
        if x <= idx <= y:
            return True
    return False

def solution(message, spoiler_ranges):
    answer = 0
    new_msg = list(message)
    for i in range(len(new_msg)):
        if check(spoiler_ranges, i) and new_msg[i] != " ":
            new_msg[i] = '*'
    won_word = message.split()
    words = []
    spo = []
    new_msg = "".join(new_msg)
    itere = new_msg.split()
    for i in range(len(itere)):
        if "*" in itere[i]:
            spo.append(won_word[i])
        else:
            words.append(itere[i])
    spo = list(set(spo))
    for c in spo:
        if c not in words:
            answer += 1
    return answer