def spliter(txt, num):
    start = -1
    end = -1
    txt = list(txt)
    for i in range(len(txt)):
        if txt[i].isdigit() and start == -1:
            start = i
        if not txt[i].isdigit() and not start == -1:
            end = i
            break
        if i == len(txt) - 1 and end == -1:
            end = i+1
            break
    
    if start == end:
        it = int(txt[start])
    else:
        it = "".join(txt[start:end])
        if len(it) > 5:
            it = it[:5]
        it = int(it)
    
    return (
        "".join(txt[:start]).lower(), 
        it,
        num
    )
            

def solution(files):
    new_files = []
    for i in range(len(files)):
        new_files.append((files[i], i+1))
    new_files.sort(key=lambda x:spliter(x[0], x[1]))
    return [x[0] for x in new_files]