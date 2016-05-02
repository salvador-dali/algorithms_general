//https://www.hackerrank.com/challenges/coin-on-the-table
package main

import (
	"bufio"
	"fmt"
	"os"
)

func readDirectionsGrid() ([][]int, int) {
	row, col, k, reader := 0, 0, 0, bufio.NewReader(os.Stdin)
	fmt.Scanf("%d %d %d", &row, &col, &k)

	M := make([][]int, row)
	a := make([]int, row*col)
	for i := range M {
		M[i] = a[i*col : (i+1)*col]
	}

	// up, right, down, left
	mapping := map[byte]int{'U': 1, 'R': 2, 'D': 3, 'L': 4, '*': 0}
	for i := 0; i < row; i++ {
		text, _ := reader.ReadString('\n')
		for j := 0; j < col; j++ {
			M[i][j] = mapping[text[j]]
		}
	}
	return M, k
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func calculateChanges(M [][]int, k int) int {
	high_num := 1000
	row, col := len(M), len(M[0])

	G := make([][]int, row)
	a := make([]int, row*col)
	for i := range G {
		G[i] = a[i*col : (i+1)*col]
	}
	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			G[i][j] = high_num
		}
	}
	G[0][0] = 0

	for t := 1; t <= k; t++ {
		values_to_be_updates := [][3]int{}
		for i := 0; i < row; i++ {
			for j := 0; j < col; j++ {
				if G[i][j] != high_num {
					neighbors := [][3]int{
						[3]int{i, j - 1, 4},
						[3]int{i, j + 1, 2},
						[3]int{i - 1, j, 1},
						[3]int{i + 1, j, 3},
					}

					for _, v := range neighbors {
						y, x, dir := v[0], v[1], v[2]
						if y >= 0 && y < row && x >= 0 && x < col {
							value := G[i][j]
							if dir != M[i][j] {
								value++
							}
							value = min(value, G[y][x])
							values_to_be_updates = append(values_to_be_updates, [3]int{y, x, value})
						}
					}
				}
			}
		}

		for _, v := range values_to_be_updates {
			G[v[0]][v[1]] = min(G[v[0]][v[1]], v[2])
		}
	}

	for i := 0; i < row; i++ {
		for j := 0; j < col; j++ {
			if M[i][j] == 0 {
				res := G[i][j]
				if res == high_num {
					return -1
				}

				return res
			}
		}
	}

	return -1
}

func main() {
	M, k := readDirectionsGrid()
	fmt.Println(calculateChanges(M, k))
}
