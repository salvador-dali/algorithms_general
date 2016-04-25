// https://www.hackerrank.com/challenges/bfsshortreach
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func BFS(G map[int]map[int]bool, start int, total int) {
	cost, seen := make([]int, total+1), make([]bool, total+1)
	frontier := []int{start}
	seen[start] = true
	for len(frontier) > 0 {
		el := frontier[0]
		frontier = frontier[1:]
		for k, _ := range G[el] {
			if !seen[k] {
				seen[k] = true
				frontier = append(frontier, k)
				cost[k] = cost[el] + 1
			}
		}
	}
	for i := 1; i < len(cost); i++ {
		if i != start {
			if cost[i] == 0 {
				fmt.Print(-1, " ")
			} else {
				fmt.Print(cost[i]*6, " ")
			}

		}
	}
	fmt.Println()
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan() // read number of test cases
	T, _ := strconv.Atoi(scanner.Text())
	for T > 0 {
		T--
		scanner.Scan()
		arr := strings.Fields(scanner.Text()) // read N and M
		N, _ := strconv.Atoi(arr[0])
		M, _ := strconv.Atoi(arr[1])
		G := map[int]map[int]bool{}
		for M > 0 {
			M--
			scanner.Scan() // read graph
			arr := strings.Fields(scanner.Text())
			num1, _ := strconv.Atoi(arr[0])
			num2, _ := strconv.Atoi(arr[1])
			if len(G[num1]) == 0 {
				G[num1] = map[int]bool{}
			}
			if len(G[num2]) == 0 {
				G[num2] = map[int]bool{}
			}
			G[num2][num1] = true
			G[num1][num2] = true
		}
		scanner.Scan() // read the starting node
		start, _ := strconv.Atoi(scanner.Text())
		BFS(G, start, N)
	}
}
