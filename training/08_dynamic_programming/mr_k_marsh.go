// https://www.hackerrank.com/challenges/mr-k-marsh/
package main

import (
	"bufio"
	"fmt"
	"os"
)

func readMatrix() [][]bool {
	n, m, reader := 0, 0, bufio.NewReader(os.Stdin)
	fmt.Scanf("%d %d", &n, &m)

	M := make([][]bool, n)
	for i := range M {
		M[i] = make([]bool, m)
	}

	for i := 0; i < n; i++ {
		text, _ := reader.ReadString('\n')
		for j := 0; j < m; j++ {
			if text[j] == '.' {
				M[i][j] = true
			}
		}
	}
	return M
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func analyze(M [][]bool) int {
	n, m := len(M), len(M[0])

	M_left := make([][]int, n)
	for i := range M {
		M_left[i] = make([]int, m)
	}

	for i := 0; i < n; i++ {
		best := -1
		for j := 0; j < m; j++ {
			if M[i][j] {
				best++
			} else {
				best = -1
			}
			M_left[i][j] = best
		}
	}

	best := 0
	for left := 0; left < m; left++ {
		for right := left + 1; right < m; right++ {
			up, down := -1, -1
			for i := 0; i < n; i++ {
				if M_left[i][right] >= right-left {
					if up == -1 {
						up = i
					}
					down = i
				}
				if down > up {
					best = max(best, down-up+right-left)
				}

				if !M[i][left] || !M[i][right] {
					up, down = -1, -1
				}
			}
		}
	}

	return best * 2
}

func main() {
	res := analyze(readMatrix())
	if res == 0 {
		fmt.Println("impossible")
	} else {
		fmt.Println(res)
	}
}
