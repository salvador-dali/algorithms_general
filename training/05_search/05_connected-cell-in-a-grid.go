// https://www.hackerrank.com/challenges/connected-cell-in-a-grid
package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
    "fmt"
)

func readMatrix() [][]bool {
	scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    scanner.Scan()
	matrix := [][]bool{}
	for scanner.Scan() {
		line := []bool{}
		for _, v := range (strings.Fields(scanner.Text())) {
			num, _ := strconv.Atoi(v)
            if num == 1{
                line = append(line, true)
            } else {
                line = append(line, false)
            }
			
		}
		matrix = append(matrix, line)
	}
	return matrix
}

func analyze(M [][]bool)int{
	checked := map[int]bool{}
	x, y, maxSoFar := len(M[0]), len(M), 0

	for i := 0; i < y; i++{
		for j := 0; j < x; j++{
			el := i * x + j
			if M[i][j] && !checked[el]{
				checked[el] = true
				fifo, num := []int{el}, 0
				for len(fifo) > 0{
					el := fifo[len(fifo) - 1]
					num++
					fifo = fifo[:len(fifo) - 1]
					y1, x1 := el / x, el % x
					if y1 < y - 1 && M[y1 + 1][x1] && !checked[el + x]{
						fifo = append(fifo, el + x)
						checked[el + x] = true
					}
					if x1 < x - 1 && M[y1][x1 + 1] && !checked[el + 1]{
						fifo = append(fifo, el + 1)
						checked[el + 1] = true
					}
					if x1 < x - 1 && y1 < y - 1 && M[y1 + 1][x1 + 1] && !checked[el + x + 1]{
						fifo = append(fifo, el + x + 1)
						checked[el + x + 1] = true
					}

					if x1 > 0 && M[y1][x1 - 1] && !checked[el - 1]{
						fifo = append(fifo, el - 1)
						checked[el - 1] = true
					}
					if x1 > 0 && y1 < y - 1 && M[y1 + 1][x1 - 1] && !checked[el + x - 1]{
						fifo = append(fifo, el + x - 1)
						checked[el + x - 1] = true
					}

					if y1 > 0 && M[y1 - 1][x1] && !checked[el - x]{
						fifo = append(fifo, el - x)
						checked[el - x] = true
					}
					if y1 > 0 && x1 < x - 1 && M[y1 - 1][x1 + 1] && !checked[el - x + 1]{
						fifo = append(fifo, el - x + 1)
						checked[el - x + 1] = true
					}
					if y1 > 0 && x1 > 0 && M[y1 - 1][x1 - 1] && !checked[el - x - 1]{
						fifo = append(fifo, el - x - 1)
						checked[el - x - 1] = true
					}
				}
				if num > maxSoFar{
					maxSoFar = num
				}
			}
		}
	}
	return maxSoFar
}

func main(){
	matrix := readMatrix()
	fmt.Println(analyze(matrix))
}
