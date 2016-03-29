//https://www.hackerrank.com/challenges/nimble-game-1
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func nim_sum(arr []int) bool {
	res := 0
	for _, v := range arr {
		res ^= v
	}
	return res != 0
}

func nimble(arr []int) bool {
	piles := []int{}
	for k, v := range arr {
		if v%2 == 1 {
			piles = append(piles, k)
		}
	}

	return nim_sum(piles)
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

		if nimble(arr) {
			fmt.Println("First")
		} else {
			fmt.Println("Second")
		}
	}
}
