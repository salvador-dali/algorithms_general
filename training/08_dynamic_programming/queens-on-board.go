package main

import (
	"fmt"
	"bufio"
	"os"
)

func readManyBooleanGrids() {
	reader, T := bufio.NewReader(os.Stdin), 0

	for fmt.Scanf("%d", &T); T > 0; T-- {
		text, _ := reader.ReadString('\n')
		tmp := [2]int{0, 0}
		for pos, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			tmp[pos] = num
		}

		row, col := tmp[0], tmp[1]
		M := make([][]int, row)
		a := make([]int, row * col)
		for i := range M {
			M[i] = a[i * col:(i + 1) * col]
		}

		for i := 0; i < row; i++ {
			text, _ := reader.ReadString('\n')
			for j := 0; j < col; j++ {
				if text[j] == '.' {
					M[i][j] = true
				}
			}
		}

		fmt.Println(M)
	}
}

func main(){
	M := readBooleanGrid()
}
