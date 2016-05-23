//https://www.hackerrank.com/challenges/vertical-rooks
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func nim(arr []int) bool {
	res := 0
	for _, v := range arr {
		res ^= v
	}
	return res != 0
}

func main() {
	T, reader := 0, bufio.NewReader(os.Stdin)
	fmt.Scanf("%d", &T)

	for i := 0; i < T; i++ {
		text, _ := reader.ReadString('\n')
		N, _ := strconv.Atoi(strings.TrimRight(text, "\n"))
		arr1, arr2 := make([]int, N), make([]int, N)
		for i := 0; i < N; i++ {
			text, _ := reader.ReadString('\n')
			num, _ := strconv.Atoi(strings.TrimRight(text, "\n"))
			arr1[i] = num
		}

		for i := 0; i < N; i++ {
			text, _ := reader.ReadString('\n')
			num, _ := strconv.Atoi(strings.TrimRight(text, "\n"))
			arr2[i] = num
		}

		stones := make([]int, N)
		for i := 0; i < N; i++ {
			stones[i] = abs(arr1[i]-arr2[i]) - 1
		}

		if nim(stones) {
			fmt.Println("player-2")
		} else {
			fmt.Println("player-1")
		}
	}
}
