// https://www.hackerrank.com/challenges/a-very-big-sum
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getSum() uint64 {
	s := uint64(0)
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	for _, v := range strings.Fields(scanner.Text()) {
		num, _ := strconv.Atoi(v)
		s += uint64(num)
	}
	return s
}

func main() {
	n := 0
	fmt.Scanf("%d", &n)
	fmt.Println(getSum())
}
