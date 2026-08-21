import "slices"
import "strconv"
import "strings"

func solution(a string, b string) string {
    a_list := []rune(a)
    b_list := []rune(b)

	slices.Reverse(a_list)
	slices.Reverse(b_list)
    
    a_len := len(a_list)
    b_len := len(b_list)
    
    var reals int
	var per int
    var reals_li []rune
    var per_li []rune
    
    if (a_len > b_len) {
		reals = a_len - 1
		per = b_len - 1
        reals_li = a_list
        per_li = b_list
	} else {
		reals = b_len - 1
        per = a_len - 1
        reals_li = b_list
        per_li = a_list
	}

    carry := 0
    var tmp int
    result := []int{}
    
    for i := 0; i <= reals; i++ {
        tmp = int(reals_li[i] - '0') + carry
        if (i <= per) {
            tmp += int(per_li[i] - '0')
        }
        carry = tmp/10
        result = append(result, tmp%10)
    }
    if (carry != 0) {
        result = append(result, carry)
    }
    slices.Reverse(result)
    answer := make([]string, len(result))
    
    for i, num := range result {
        answer[i] = strconv.Itoa(num)
    }
    
    return strings.Join(answer, "")
}