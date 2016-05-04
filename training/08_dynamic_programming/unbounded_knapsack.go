//https://www.hackerrank.com/challenges/unbounded-knapsack
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func knapsack_unbounded(prices []int, goal int) int {
	sort.Ints(prices)
	arr, n, prev := make([]int, len(prices)), 0, -1
	for _, v := range prices {
		if v != prev {
			if goal%v == 0 {
				return goal
			}
			arr[n], prev, n = v, v, n+1
		}
	}

	prices = arr[:n]

	row, col := goal+1, n+1
	M := make([][]bool, row)
	e := make([]bool, row*col)
	for i := range M {
		M[i] = e[i*col : (i+1)*col]
	}

	for i := 0; i < col; i++ {
		M[0][i] = true
	}

	for i := 1; i < row; i++ {
		for j := 1; j < col; j++ {
			M[i][j] = M[i][j-1]
			if i >= prices[j-1] {
				M[i][j] = M[i][j] || M[i-prices[j-1]][j]
			}
		}
	}

	for i := row - 1; i >= 0; i-- {
		if M[i][col-1] {
			return i
		}
	}

	return 0
}

func main() {
	T, reader := 0, bufio.NewReader(os.Stdin)
	for fmt.Scanf("%d", &T); T > 0; T-- {
		text, _ := reader.ReadString('\n')

		tmp := [2]int{}
		for i, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			tmp[i] = num
		}

		arr := make([]int, tmp[0])
		text, _ = reader.ReadString('\n')
		for i, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			arr[i] = num
		}

		fmt.Println(knapsack_unbounded(arr, tmp[1]))
	}
}
