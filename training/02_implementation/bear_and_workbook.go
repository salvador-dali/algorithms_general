package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readArray() (int, []int) {
	reader, arr, n, k := bufio.NewReader(os.Stdin), []int{}, 0, 0
	fmt.Scanf("%d %d", &n, &k)
	text, _ := reader.ReadString('\n')
	for _, v := range strings.Fields(text) {
		num, _ := strconv.Atoi(v)
		arr = append(arr, num)
	}
	return k, arr
}

func find_special(t []int, k int) int {
	curr_page, special_found := 1, 0
	for _, v := range t {
		for i := 1; i <= v; i++ {
			if i == curr_page {
				special_found += 1
			}
			if i%k == 0 {
				curr_page += 1
			}
		}
		if v%k > 0 {
			curr_page += 1
		}
	}
	return special_found
}

func main() {
	k, t := readArray()
	fmt.Println(find_special(t, k))
}
