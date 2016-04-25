// https://www.hackerrank.com/challenges/floyd-city-of-blinding-lights
//let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
// for each vertex v
//    dist[v][v] ← 0
// for each edge (u,v)
//    dist[u][v] ← w(u,v)  // the weight of the edge (u,v)
// for k from 1 to |V|
//    for i from 1 to |V|
//       for j from 1 to |V|
//          if dist[i][j] > dist[i][k] + dist[k][j]
//              dist[i][j] ← dist[i][k] + dist[k][j]
//          end if
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func floyd(G map[int]map[int]int, N int) [][]int {
	inf := 99999999
	matrix := [][]int{}
	for i := 0; i < N; i++ {
		line := make([]int, N)
		for j := 0; j < N; j++ {
			line[j] = inf
		}
		matrix = append(matrix, line)
	}

	for i := 0; i < N; i++ {
		matrix[i][i] = 0
	}

	for v1, arr := range G {
		for v2, w := range arr {
			matrix[v1-1][v2-1] = w
		}
	}

	for k := 0; k < N; k++ {
		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
				if matrix[i][j] > matrix[i][k]+matrix[k][j] {
					matrix[i][j] = matrix[i][k] + matrix[k][j]
				}
			}
		}
	}

	return matrix
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	arr := strings.Fields(scanner.Text()) // read N and M
	N, _ := strconv.Atoi(arr[0])
	M, _ := strconv.Atoi(arr[1])
	G := map[int]map[int]int{}
	for M > 0 {
		M--
		scanner.Scan()
		arr := strings.Fields(scanner.Text())
		num1, _ := strconv.Atoi(arr[0])
		num2, _ := strconv.Atoi(arr[1])
		weight, _ := strconv.Atoi(arr[2])
		if len(G[num1]) == 0 {
			G[num1] = map[int]int{}
		}
		G[num1][num2] = weight
	}
	matrix := floyd(G, N)
	scanner.Scan()
	Q, _ := strconv.Atoi(scanner.Text())
	inf := 99999999
	for Q > 0 {
		Q--
		scanner.Scan()
		arr := strings.Fields(scanner.Text())
		v1, _ := strconv.Atoi(arr[0])
		v2, _ := strconv.Atoi(arr[1])
		ans := matrix[v1-1][v2-1]
		if ans == inf {
			fmt.Println(-1)
		} else {
			fmt.Println(ans)
		}
	}
}
