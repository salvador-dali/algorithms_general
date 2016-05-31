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
	return res == 0
}

func main() {
	T, reader := 0, bufio.NewReader(os.Stdin)
	for fmt.Scanf("%d", &T); T > 0; T-- {
		text, _ := reader.ReadString('\n')
		num, _ := strconv.Atoi(strings.TrimRight(text, "\n"))
		arr := make([]int, num)

		text, _ = reader.ReadString('\n') // '\r'
		for i, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			arr[i] = num
		}

		if nim_sum(arr) {
			fmt.Println("Second")
		} else {
			fmt.Println("First")
		}
	}
}
