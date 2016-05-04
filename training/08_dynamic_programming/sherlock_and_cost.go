//https://www.hackerrank.com/challenges/sherlock-and-cost
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func abs(a int) int {
	if a > 0 {
		return a
	}
	return -a
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func best_value(arr []int) int {
	lo, hi := 0, 0
	for i := 1; i < len(arr); i++ {
		lo, hi = max(arr[i-1]-1+hi, lo), max(arr[i]-1+lo, abs(arr[i]-arr[i-1])+hi)
	}

	return max(lo, hi)
}

func main() {
	T, reader := 0, bufio.NewReader(os.Stdin)
	for fmt.Scanf("%d", &T); T > 0; T-- {
		text, _ := reader.ReadString('\n')
		num, _ := strconv.Atoi(strings.TrimRight(text, "\n"))
		arr := make([]int, num)

		text, _ = reader.ReadString('\n')
		for i, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			arr[i] = num
		}
		fmt.Println(best_value(arr))
	}
}
