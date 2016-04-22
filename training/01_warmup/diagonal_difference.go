// https://www.hackerrank.com/challenges/diagonal-difference
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readMatrix() [][]int {
	scanner := bufio.NewScanner(os.Stdin)
	matrix := [][]int{}
	for scanner.Scan() {
		line := []int{}
		for _, v := range strings.Fields(scanner.Text()) {
			num, _ := strconv.Atoi(v)
			line = append(line, num)
		}
		matrix = append(matrix, line)
	}
	return matrix
}

func main() {
	n := 0
	fmt.Scanf("%d", &n)
	matrix := readMatrix()

	l1, l2 := 0, 0
	for i := 0; i < n; i++ {
		l1 += matrix[i][i]
		l2 += matrix[i][n-i-1]
	}

	if l1 > l2 {
		fmt.Println(l1 - l2)
	} else {
		fmt.Println(l2 - l1)
	}
}
