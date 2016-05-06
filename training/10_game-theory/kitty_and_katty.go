//https://www.hackerrank.com/challenges/kitty-and-katty
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func isFirstWin(n int) bool {
	if n == 1 {
		return true
	}

	return n%2 == 0
}

func main() {
	T := 0
	fmt.Scanf("%d\n", &T)
	reader := bufio.NewReader(os.Stdin)
	for i := 0; i < T; i++ {
		text, _ := reader.ReadString('\n')
		num, _ := strconv.Atoi(strings.TrimRight(text, "\n\r"))
		if isFirstWin(num) {
			fmt.Println("Kitty")
		} else {
			fmt.Println("Katty")
		}
	}
}
