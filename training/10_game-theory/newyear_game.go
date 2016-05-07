// https://www.hackerrank.com/challenges/newyear-game
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	T, reader := 0, bufio.NewReader(os.Stdin)
	for fmt.Scanf("%d", &T); T > 0; T-- {
		text, _ := reader.ReadString('\r')

		arr := [3]int{}
		text, _ = reader.ReadString('\r')
		for _, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			arr[num%3]++
		}

		if arr[1]%2 == 0 && arr[2]%2 == 0 {
			fmt.Println("Koca")
		} else {
			fmt.Println("Balsa")
		}
	}
}
