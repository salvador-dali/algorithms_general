//https://www.hackerrank.com/challenges/tower-breakers-1
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func calc(n, m int) int {
	if m == 1 {
		return 2
	}

	if n%2 == 1 {
		return 1
	}

	return 2
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
		N, M := tmp[0], tmp[1]
		fmt.Println(calc(N, M))
	}
}
