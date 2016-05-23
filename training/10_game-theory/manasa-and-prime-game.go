/*
https://www.hackerrank.com/challenges/manasa-and-prime-game
find the period of grundy function using games.py code
*/
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func subtraction(arr []int) bool {
	period := []int{0, 0, 1, 1, 2, 2, 3, 3, 4}
	n, nim_sum := len(period), 0
	for _, v := range arr {
		nim_sum ^= period[v%n]
	}

	return nim_sum != 0
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
		if subtraction(arr) {
			fmt.Println("Manasa")
		} else {
			fmt.Println("Sandy")
		}
	}
}
