func solution(num int) int {
    now := num
    for i := range 500 {
        if (now == 1) {
            return i
        }
        if (now % 2 == 0) {
            now = now / 2
        } else {
            now = now * 3 + 1
        }
    }
    return -1
}