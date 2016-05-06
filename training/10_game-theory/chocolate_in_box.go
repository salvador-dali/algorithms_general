// https://www.hackerrank.com/challenges/chocolate-in-box
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func arr_xor(arr []int) int {
	x, s := 0, 0
	for _, v := range arr {
		x ^= v
	}
	if x == 0 {
		return 0
	}

	for _, v := range arr {
		a := x ^ v
		if a < v {
			s++
		}
	}
	return s
}

func main() {
	T := 0
	fmt.Scanf("%d", &T)

	reader, arr := bufio.NewReader(os.Stdin), make([]int, T)
	text, _ := reader.ReadString('\n')
	for i, v := range strings.Fields(text) {
		num, _ := strconv.Atoi(v)
		arr[i] = num
	}

	fmt.Println(arr_xor(arr))
}
