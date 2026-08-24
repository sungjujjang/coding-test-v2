func solution(a int, b int) int {
    if (a > b) {
        tmp := a
        a = b
        b = tmp
    }
    ans := 0
    for i := a; i <= b; i++ {
        ans += i        
    }
    return ans
}