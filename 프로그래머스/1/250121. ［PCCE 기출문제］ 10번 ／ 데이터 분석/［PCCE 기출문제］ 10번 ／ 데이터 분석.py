MAPPING = {
    "code": 0,
    "date": 1,
    "maximum": 2,
    "remain": 3
}

def solution(data, ext, val_ext, sort_by):
    new_data = []
    for d in data:
        if d[MAPPING[ext]] < val_ext:
            new_data.append(d)
    new_data.sort(key=lambda x: x[MAPPING[sort_by]])
    return new_data