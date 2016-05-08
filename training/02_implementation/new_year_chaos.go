package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func calc(arr []int) int {
	cnt := 0
	for i := 0; i < len(arr); i++ {
		diff := arr[i] - i - 1
		if diff > 2 {
			return -1
		}

		tmp, pos := arr[i], i
		for j := i - 1; j >= 0; j-- {
			if arr[j] < tmp {
				break
			} else {
				arr[pos] = arr[j]
				arr[j] = tmp
				pos--
				if diff <= 0 {
					cnt++
				}
			}
		}
	}

	return cnt
}

func main() {
	T, reader := 0, bufio.NewReader(os.Stdin)
	for fmt.Scanf("%d", &T); T > 0; T-- {
		text, _ := reader.ReadString('\r')
		num, _ := strconv.Atoi(strings.Trim(text, "\n\r"))
		arr := make([]int, num)

		text, _ = reader.ReadString('\r')
		for i, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			arr[i] = num
		}
		res := calc(arr)
		if res == -1 {
			fmt.Println("Too chaotic")
		} else {
			fmt.Println(res)
		}
	}
}
