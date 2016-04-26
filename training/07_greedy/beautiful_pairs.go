package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readOneArray() ([]int, []int) {
	T := 0
	fmt.Scanf("%d", &T)

	reader := bufio.NewReader(os.Stdin)
	arr1, arr2 := make([]int, T), make([]int, T)

	text, _ := reader.ReadString('\n')
	for i, v := range strings.Fields(text) {
		num, _ := strconv.Atoi(v)
		arr1[i] = int(num)
	}

	text, _ = reader.ReadString('\n')
	for i, v := range strings.Fields(text) {
		num, _ := strconv.Atoi(v)
		arr2[i] = int(num)
	}

	return arr1, arr2
}

func findSolution(a1, a2 []int) int {
	m1, m2 := map[int]int{}, map[int]int{}
	for _, v := range a1 {
		m1[v]++
	}

	for _, v := range a2 {
		m2[v]++
	}

	cnt, changed := 0, false
	for k, v1 := range m1 {
		v2, ok := m2[k]
		if !ok && !changed {
			cnt++
			changed = true
		}
		if v1 <= v2 {
			cnt += v1
		}
	}

	if !changed {
		cnt--
	}
	return cnt
}

func main() {
//	arr1 := []int{1, 1, 1, 1, 2, 2, 3}
//	arr2 := []int{1, 1, 1, 1, 2, 2, 2}
	arr1 := []int{1, 2, 3}
	arr2 := []int{1, 2, 2}
	findSolution(arr1, arr2)

}
