// https://www.hackerrank.com/challenges/stone-piles
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func grundy_inf(arr []int) bool {
	first_grundy, res := []int{0, 0, 0, 1, 0, 2, 3, 4, 0}, 0
	for _, v := range arr {
		if v < len(first_grundy) {
			res ^= first_grundy[v]
		} else {
			res ^= v - 4
		}
	}
	return res != 0
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
		if grundy_inf(arr) {
			fmt.Println("ALICE")
		} else {
			fmt.Println("BOB")
		}
	}
}
