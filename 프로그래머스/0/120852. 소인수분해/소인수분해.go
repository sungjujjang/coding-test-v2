func solution(n int) []int {
	var answer []int
	d := 2

	for d*d <= n {
		if n%d == 0 {
			if len(answer) == 0 || answer[len(answer)-1] != d {
				answer = append(answer, d)
			}
			n /= d
		} else {
			d++
		}
	}

	if n > 1 {
		if len(answer) == 0 || answer[len(answer)-1] != n {
			answer = append(answer, n)
		}
	}

	return answer
}
