// https://www.hackerrank.com/challenges/cut-the-tree
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readWeightedTree() (map[int][]int, []int) {
	reader := bufio.NewReader(os.Stdin)
	tmp, _ := reader.ReadString('\n')
	vertex_num, _ := strconv.Atoi(strings.TrimRight(tmp, "\n"))

	tmp, _ = reader.ReadString('\n')
	weights := []int{0}
	for _, v := range strings.Fields(strings.TrimRight(tmp, "\n")) {
		num, _ := strconv.Atoi(v)
		weights = append(weights, num)
	}

	G := map[int][]int{}
	for i := 1; i < vertex_num; i++ {
		tmp, _ = reader.ReadString('\n')
		two_vertex := [2]int{}
		for i, v := range strings.Fields(strings.TrimRight(tmp, "\n")) {
			num, _ := strconv.Atoi(v)
			two_vertex[i] = num
		}
		G[two_vertex[0]] = append(G[two_vertex[0]], two_vertex[1])
		G[two_vertex[1]] = append(G[two_vertex[1]], two_vertex[0])
	}
	return G, weights
}

func createRootedTree(G map[int][]int, root int) map[int][]int {
	rooted, frontier, seen := map[int][]int{}, []int{root}, map[int]bool{root: true}
	for {
		if len(frontier) == 0 {
			return rooted
		}

		next_frontier := []int{}
		for _, v := range frontier {
			children, _ := G[v]
			for _, child := range children {
				if !seen[child] {
					seen[child] = true
					rooted[v] = append(rooted[v], child)
					next_frontier = append(next_frontier, child)
				}
			}
		}
		frontier = next_frontier
	}
	return rooted
}

func recursiveWeightsSum(root int, G map[int][]int, weights []int, weights_rooted []int) int {
	children, _ := G[root]
	sum := weights[root]
	for _, child := range children {
		sum += recursiveWeightsSum(child, G, weights, weights_rooted)
	}

	weights_rooted[root] = sum
	return sum
}

func abs(x int) int {
	if x > 0 {
		return x
	}
	return -x
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func find_diff(G map[int][]int, root int, weights_rooted []int) int {
	frontier, total_weight := []int{root}, weights_rooted[1]
	smallest_diff := total_weight
	for {
		if len(frontier) == 0 {
			return smallest_diff
		}

		next_frontier := []int{}
		for _, v := range frontier {
			children, _ := G[v]
			for _, child := range children {
				smallest_diff = min(smallest_diff, abs(total_weight-2*weights_rooted[child]))
				next_frontier = append(next_frontier, child)
			}
		}
		frontier = next_frontier
	}
}

func main() {
	G, weights := readWeightedTree()
	weights_rooted := make([]int, len(weights), len(weights))

	rooted := createRootedTree(G, 1)
	recursiveWeightsSum(1, rooted, weights, weights_rooted)
	res := find_diff(rooted, 1, weights_rooted)
	fmt.Println(res)
}
