package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	T, K := 0, 0
	fmt.Scanf("%d %d", &T, &K)

	reader := bufio.NewReader(os.Stdin)
	h, c := make([]int, T), make([]int, T)
	for i := 0; i < T; i++ {
		text, _ := reader.ReadString('\n')
		tmp := [2]int{0, 0}
		for pos, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			tmp[pos] = num
		}

		h[i], c[i] = tmp[0], tmp[1]
	}

	fmt.Println(K)
	fmt.Println(h)
	fmt.Println(c)
}
