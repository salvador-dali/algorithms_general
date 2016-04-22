// https://www.hackerrank.com/challenges/bear-and-steady-gene

package main

import (
	"fmt"
	"time"
)

func valid(arr [4]int, n int) bool {
	return arr[0] <= n && arr[1] <= n && arr[2] <= n && arr[3] <= n
}

func find_pos(s string) int {
	arr, n, max_index := [4]int{0, 0, 0, 0}, len(s), 0
	limit, res := n/4, n
	for i := n - 1; i >= 0; i-- {
		if s[i] == 'A' {
			arr[0] += 1
		} else if s[i] == 'C' {
			arr[1] += 1
		} else if s[i] == 'G' {
			arr[2] += 1
		} else if s[i] == 'T' {
			arr[3] += 1
		}
		if !valid(arr, limit) {
			max_index = i + 1
			if s[i] == 'A' {
				arr[0] -= 1
			} else if s[i] == 'C' {
				arr[1] -= 1
			} else if s[i] == 'G' {
				arr[2] -= 1
			} else if s[i] == 'T' {
				arr[3] -= 1
			}
			break
		}
	}

	for min_index := -1; min_index < n-1 && max_index < n && min_index < max_index; min_index++ {
		for ; !valid(arr, limit) && max_index < n; max_index++ {
			if s[max_index] == 'A' {
				arr[0]--
			} else if s[max_index] == 'C' {
				arr[1]--
			} else if s[max_index] == 'G' {
				arr[2]--
			} else if s[max_index] == 'T' {
				arr[3]--
			}
		}

		if max_index > n || !valid(arr, limit) {
			break
		}

		s_len := 0
		if max_index-min_index-1 > 0 {
			s_len = max_index - min_index - 1
		}

		if s_len < res {
			res = s_len
		}

		if s[min_index+1] == 'A' {
			arr[0]++
		} else if s[min_index+1] == 'C' {
			arr[1]++
		} else if s[min_index+1] == 'G' {
			arr[2]++
		} else if s[min_index+1] == 'T' {
			arr[3]++
		}
	}
	return res
}

func main() {
	s, n := "", 0
	fmt.Scanf("%d", &n)
	fmt.Scanf("%s", &s)
	fmt.Println(find_pos(s))
}
