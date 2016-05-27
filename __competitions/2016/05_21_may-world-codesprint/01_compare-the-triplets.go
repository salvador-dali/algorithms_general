// https://www.hackerrank.com/contests/may-world-codesprint/challenges/compare-the-triplets
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	arr1, arr2 := make([]int, 3), make([]int, 3)

	text, _ := reader.ReadString('\n')
	for i, v := range strings.Fields(text) {
		num, _ := strconv.Atoi(v)
		arr1[i] = num
	}

	text, _ = reader.ReadString('\n')
	for i, v := range strings.Fields(text) {
		num, _ := strconv.Atoi(v)
		arr2[i] = num
	}

	a, b := 0, 0
	for i := 0; i < 3; i++ {
		if arr1[i] > arr2[i] {
			a++
		} else if arr1[i] < arr2[i] {
			b++
		}
	}

	fmt.Println(a, b)
}
