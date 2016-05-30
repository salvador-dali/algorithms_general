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

/**
in any number of towers, for M = 1, second wins

one tower. M =
2		first wins
3 ...	first wins by reducing the tower to 1 on the first move


Two towers. M =
2		second wins
3 ...	second wins by doing the same move on another tower

Three towers. M =
2		first wins
3		first wins
4 ...	first wins by removing all elements from one tower. He reduces the problem to 2 towers where
		the second moves first.

Four towers. M =
2		second wins
3		second wins

4 4 4 4
2 4 4 4
2 2 4 4
2 2 2 4
*/
