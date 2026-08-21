func solution(arr []int, querys []int) []int {
    tmp := arr
    for idx, query := range querys {
        if (idx % 2 == 0) {
            tmp = tmp[:query+1]
        } else {
            tmp = tmp[query:]
        }
    }
    return tmp
}