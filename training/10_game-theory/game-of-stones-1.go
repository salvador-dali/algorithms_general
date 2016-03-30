//https://www.hackerrank.com/challenges/game-of-stones-1
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func preCalc(n int) []bool {
	res := make([]bool, n+1)
	for i := 2; i <= 6; i++ {
		res[i] = true
	}

	for i := 7; i <= n; i++ {
		can_guarantee_win := res[i-2]
		can_guarantee_win = can_guarantee_win && res[i-3]
		can_guarantee_win = can_guarantee_win && res[i-5]
		res[i] = !can_guarantee_win
	}
	return res
}

func main() {
	T, res := 0, preCalc(105)
	fmt.Scanf("%d", &T)

	reader := bufio.NewReader(os.Stdin)
	for i := 0; i < T; i++ {
		text, _ := reader.ReadString('\n')
		num, _ := strconv.Atoi(strings.TrimRight(text, "\n"))
		if res[num] {
			fmt.Println("First")
		} else {
			fmt.Println("Second")
		}
	}
}
