func solution(numbers string) int64 {
    start := 0
    offset := 3
    number := map[string]int64{
        "zero":  0,
        "one":   1,
        "two":   2,
        "three": 3,
        "four":  4,
        "five":  5,
        "six":   6,
        "seven": 7,
        "eight": 8,
        "nine":  9,
    }
    var answer int64 = 0
    for i := 0; i < len(numbers); i++ {
        if (start+offset > len(numbers)) {
            break
        }
        tmp := numbers[start:start+offset]
        value, exist := number[tmp]
        if (exist) {
            answer += value
            answer *= 10
            start += offset
            offset = 3
        } else {
            offset += 1
        }
    }
    answer /= 10
    return answer
}