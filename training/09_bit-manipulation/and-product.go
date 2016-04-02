//https://www.hackerrank.com/challenges/and-product
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func and_range(a, b int) int {
	tmp, mul, pos, small_number, res := a, 1, 0, 0, 0
	for tmp > 0 {
		is_one := tmp % 2
		tmp, pos = tmp/2, pos+1
		if is_one == 1 {
			if a+mul-small_number > b {
				res += mul
			}
		}
		mul, small_number = mul*2, small_number+is_one*mul
	}
	return res
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
		fmt.Println(and_range(tmp[0], tmp[1]))
	}
}
