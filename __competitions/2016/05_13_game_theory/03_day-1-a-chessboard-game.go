package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func investigation() {
	// this is O(n * n) solution which helped to find a pattern
	n := 15
	M := make([][]int, n)
	e := make([]int, n*n)
	for i := range M {
		M[i] = e[i*n : (i+1)*n]
	}

	for i := 2; i < n; i++ {
		for j := 0; j <= i; j++ {
			x1, y1 := i-j, j
			is_any_zero := false
			for _, v := range [][2]int{
				[2]int{x1 - 2, y1 + 1},
				[2]int{x1 - 2, y1 - 1},
				[2]int{x1 + 1, y1 - 2},
				[2]int{x1 - 1, y1 - 2},
			} {
				x, y := v[0], v[1]
				if x >= 0 && y >= 0 && x < n && y < n {
					if M[y][x] == 0 {
						is_any_zero = true
						break
					}
				}
			}

			if is_any_zero {
				M[y1][x1] = 1
			} else {
				M[y1][x1] = 0
			}
		}
	}

	for _, v := range M {
		fmt.Println(v)
	}
}

func main() {
	T, reader := 0, bufio.NewReader(os.Stdin)
	fmt.Scanf("%d", &T)
	for i := 0; i < T; i++ {
		text, _ := reader.ReadString('\n')
		tmp := [2]int{0, 0}
		for pos, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			tmp[pos] = num
		}
		x, y := tmp[0]-1, tmp[1]-1

		if x%4 < 2 && y%4 < 2 {
			fmt.Println("Second")
		} else {
			fmt.Println("First")
		}
	}
}
