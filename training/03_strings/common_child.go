//https://www.hackerrank.com/challenges/common-child
package main

import (
	"fmt"
)

func longestCommonSubsequence(s1, s2 string) int {
	n, m := len(s1), len(s2)
	matrix := make([][]int, n+1)
	for i := range matrix {
		matrix[i] = make([]int, m+1)
	}

	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			best := matrix[i-1][j]
			if matrix[i][j-1] > best {
				best = matrix[i][j-1]
			}

			attempt := matrix[i-1][j-1]
			if s1[i-1] == s2[j-1] {
				attempt++
			}
			if attempt > best {
				best = attempt
			}
			matrix[i][j] = best
		}
	}

	return matrix[n][m]
}

func main() {
	s1, s2 := "", ""
	fmt.Scanf("%s", &s1)
	fmt.Scanf("%s", &s2)

	fmt.Println(longestCommonSubsequence(s1, s2))
}
