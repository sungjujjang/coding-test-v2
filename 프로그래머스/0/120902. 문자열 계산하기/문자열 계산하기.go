import "strings"
import "strconv"

func solution(my_string string) int {
    sol := strings.Split(my_string, " ")
    arr := make([]int, len(sol))
    for i, v := range sol {
        if i%2 == 0 {
            value, _ := strconv.Atoi(v)
            arr[i] = value
        }
    }
    for i, p := range sol {
        if i%2 == 1 {
            switch p {
                case "+":
                    arr[i+1] = arr[i-1] + arr[i+1]
                case "-":
                    arr[i+1] = arr[i-1] - arr[i+1]
            }
        }
    }
    return arr[len(sol)-1]
}

