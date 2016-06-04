package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Data struct {
	s  int
	a1 int
	a2 int
}
type ByS []Data

func (a ByS) Len() int           { return len(a) }
func (a ByS) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByS) Less(i, j int) bool { return a[i].s > a[j].s }

func whoWins(arr1, arr2 []int) int {
	// 0 - draw, 1 first win, -1 second win
	data := make([]Data, len(arr1))
	for i := 0; i < len(arr1); i++ {
		data[i] = Data{arr1[i] + arr2[i], arr1[i], arr2[i]}
	}

	sort.Sort(ByS(data))
	p1, p2 := 0, 0
	for i := 0; i < len(arr1); i++ {
		if i%2 == 0 {
			p1 += data[i].a1
		} else {
			p2 += data[i].a2
		}
	}

	if p1 == p2 {
		return 0
	}
	if p1 > p2 {
		return 1
	}
	return -1
}

func main() {
	T, reader := 0, bufio.NewReader(os.Stdin)
	fmt.Scanf("%d", &T)
	for i := 0; i < T; i++ {
		text, _ := reader.ReadString('\n')
		num, _ := strconv.Atoi(strings.TrimRight(text, "\n"))

		arr1, arr2 := make([]int, num), make([]int, num)
		text, _ = reader.ReadString('\n')
		for i, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			arr1[i] = num
		}

		text, _ = reader.ReadString('\n')
		for i, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			arr2[i] = num
		}

		res := whoWins(arr1, arr2)
		if res == 0 {
			fmt.Println("Tie")
		} else if res == 1 {
			fmt.Println("First")
		} else {
			fmt.Println("Second")
		}
	}
}
