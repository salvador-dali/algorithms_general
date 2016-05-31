package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func nim_sum_misere(arr []int) bool {
	// is first winning
	res, max := 0, 0
	for _, v := range arr {
		res ^= v
		if v > max {
			max = v
		}
	}

	if max == 1 {
		return len(arr)%2 == 0
	}

	return !(res == 0 && max > 1)
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
		if nim_sum_misere(arr) {
			fmt.Println("First")
		} else {
			fmt.Println("Second")
		}
	}
}
