package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func permutation_sign(arr []int) int {
	total := 0
	for i := 0; i < len(arr); i++ {
		for j := i + 1; j < len(arr); j++ {
			if arr[i] > arr[j] {
				total += 1
			}
		}
	}
	if total%2 == 1 {
		return -1
	}
	return 1
}

func main() {
	T, reader := 0, bufio.NewReader(os.Stdin)
	fmt.Scanf("%d", &T)
	for ; T > 0; T-- {
		_, _ = reader.ReadString('\n')
		text, _ := reader.ReadString('\n')
		arr := []int{}
		for _, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			arr = append(arr, num)
		}
		fmt.Println(permutation_sign(arr))
	}
}
