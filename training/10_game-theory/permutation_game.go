// https://www.hackerrank.com/challenges/permutation-game
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var global = map[string]bool{}

func serializeArr(arr []int) string {
	tmp := make([]string, len(arr))
	for k, v := range arr {
		tmp[k] = strconv.Itoa(v)
	}
	return strings.Join(tmp, ".")
}

func isIncreasing(arr []int) bool {
	if len(arr) < 2 {
		return true
	}

	for i := 0; i < len(arr)-1; i++ {
		if arr[i] > arr[i+1] {
			return false
		}
	}

	return true
}

func getChildren(arr []int) [][]int {
	children := [][]int{}

	for i := 0; i < len(arr); i++ {
		last, tmp := 0, make([]int, len(arr)-1)
		for k, v := range arr {
			if k != i {
				tmp[last] = v
				last++
			}
		}
		children = append(children, tmp)
	}

	return children
}

func isFirstWin(arr []int) bool {
	s := serializeArr(arr)
	if res, ok := global[s]; ok {
		return res
	}

	if isIncreasing(arr) {
		return false
	}

	for i := 0; i < len(arr); i++ {
		last, tmp := 0, make([]int, len(arr)-1)
		for k, v := range arr {
			if k != i {
				tmp[last] = v
				last++
			}
		}

		if !isFirstWin(tmp) {
			global[s] = true
			return true
		}
	}
	global[s] = false
	return false
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
		if isFirstWin(arr) {
			fmt.Println("Alice")
		} else {
			fmt.Println("Bob")
		}
	}
}
