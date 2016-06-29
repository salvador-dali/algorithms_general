package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func brute_one(n int, arr [][2]int, d int) int {
	occupied, total_days := make([]bool, n), 0
	for _, v := range arr {
		r, l := v[0], v[1]
		if l-r+1 >= d {
			can_proceed := true
			for i := r - 1; i < l; i++ {
				if occupied[i] {
					can_proceed = false
					break
				}
			}

			if can_proceed {
				for i := r - 1; i < l; i++ {
					occupied[i] = true
				}
				total_days += l - r + 1
			}
		}
	}
	return total_days
}

func brute_all(D int, arr [][2]int, d []int) []int {
	res := make([]int, len(d))
	for i, el := range d {
		res[i] = brute_one(D, arr, el)
	}
	return res
}

func writeManyNumbers(numbers []int) {
	var buffer bytes.Buffer
	for _, v := range numbers {
		buffer.WriteString(strconv.Itoa(v) + "\n")
	}
	fmt.Print(buffer.String())
}

func main() {
	N, D, K := 0, 0, 0
	fmt.Scanf("%d %d %d", &N, &D, &K)
	reader, arr, d := bufio.NewReader(os.Stdin), make([][2]int, N), make([]int, K)
	for i := 0; i < N; i++ {
		text, _ := reader.ReadString('\n')
		tmp := [2]int{0, 0}
		for pos, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			tmp[pos] = num
		}
		arr[i] = tmp
	}

	for i := 0; i < K; i++ {
		text, _ := reader.ReadString('\n')
		num, _ := strconv.Atoi(strings.TrimRight(text, "\n"))
		d[i] = num
	}

	writeManyNumbers(brute_all(D, arr, d))
}
