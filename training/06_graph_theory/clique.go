// https://www.hackerrank.com/challenges/clique
// http://math.stackexchange.com/q/1753723/50804
// http://en.wikipedia.org/wiki/Tur%C3%A1n_graph
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func turan(v, r int) int {
	div, mod := v/r, v%r
	tmp := v*v - mod*(div+1)*(div+1) - (r-mod)*div*div
	return tmp / 2
}

func minimum_size(n, m int) int {
	lo, hi := 1, n+1
	for lo+1 < hi {
		mid := (lo + hi) / 2
		e := turan(n, mid)
		if e < m {
			lo = mid
		} else {
			hi = mid
		}
	}
	return hi
}

func main() {
	T, reader := 0, bufio.NewReader(os.Stdin)
	for fmt.Scanf("%d", &T); T > 0; T-- {
		text, _ := reader.ReadString('\n')
		tmp := [2]int{0, 0}
		for i, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			tmp[i] = num
		}
		fmt.Println(minimum_size(tmp[0], tmp[1]))
	}
}
