//https://www.hackerrank.com/challenges/journey-to-the-moon
//get all the connected components with their size
//having an array of all connected components
//[1, 3, 2] 		- size 3
//[4, 5, 6, 7]	- size 4
//[8]			- size 1
//
//the number of pairs is:
//3 * (4 + 1) + 4 * 1 + 1 * 0
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func connectedComponents(G map[int]map[int]bool, N int) [][]int {
	components := [][]int{}
	unseen := map[int]bool{}
	for i := 0; i < N; i++ {
		unseen[i] = true
	}

	for len(unseen) > 0 {
		frontier := []int{}
		for k, _ := range unseen {
			frontier = append(frontier, k)
			break
		}

		component := []int{}
		for len(frontier) > 0 {
			element := frontier[len(frontier)-1]
			frontier = frontier[:len(frontier)-1]
			component = append(component, element)
			delete(unseen, element)
			for k, _ := range G[element] {
				if unseen[k] {
					frontier = append(frontier, k)
					delete(unseen, k)
				}
			}
		}
		components = append(components, component)
	}
	return components
}

func analyse(arr []int, total int) int {
	res := 0
	for _, v := range arr {
		total -= v
		res += v * total
	}

	return res
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	arr := strings.Fields(scanner.Text())
	N, _ := strconv.Atoi(arr[0])
	G := map[int]map[int]bool{}
	for scanner.Scan() {
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
	sizes, total := []int{}, 0
	for _, v := range connectedComponents(G, N) {
		//fmt.Println(v)
		sizes = append(sizes, len(v))
		total += len(v)
	}
	//fmt.Println()
	fmt.Println(analyse(sizes, total))
}
