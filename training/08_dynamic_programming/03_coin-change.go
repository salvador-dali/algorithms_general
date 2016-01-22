//https://www.hackerrank.com/challenges/coin-change/
package main

import (
	"fmt"
	"bufio"
	"strconv"
	"strings"
    "os"
)

func readArr() []int {
	arr, scanner := []int{}, bufio.NewScanner(os.Stdin)
	scanner.Scan()
	for _, v := range (strings.Fields(scanner.Text())) {
		num, _ := strconv.Atoi(v)
		arr = append(arr, int(num))
	}
	return arr
}

func change(n int, coins []int)int{
	answers := make([]int, n + 1)
	answers[0] = 1

	for _, coin := range(coins){
		for i := coin; i <= n; i++{
			answers[i] += answers[i - coin]
		}
	}
	return answers[len(answers) - 1]
}

func main(){
    n, m := 0, 0
    fmt.Scanf("%d %d", &n, &m)
	coins := readArr()
	res := change(n, coins)
	fmt.Println(res)
}
