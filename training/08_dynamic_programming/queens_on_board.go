package main

// 5 - obstacle
// 0 - empty space
// 1 - some queen control this space
// 2 - queen

import (
	//	"bufio"
	"fmt"
	//	"os"
	"strconv"
	"strings"
	//	"time"
)

var global_map = make(map[string]bool)

func arr_string(arr []int) string {
	arr2 := make([]string, len(arr))
	for i := 0; i < len(arr); i++ {
		arr2[i] = strconv.Itoa(arr[i])
	}

	return strings.Join(arr2, ",")
}

func printBoard(M [][]rune) {
	for _, v := range M {
		fmt.Println(v)
	}
	fmt.Println()
}

func copyPosition(M [][]rune) [][]rune {
	row, col := len(M), len(M[0])
	M1 := make([][]rune, row)
	a := make([]rune, row*col)
	for i := range M1 {
		M1[i] = a[i*col : (i+1)*col]
	}

	for i := 0; i < row; i++ {
		copy(M1[i], M[i])
	}
	return M1
}

func putQueen(M [][]rune, y, x int) string {
	// put a queen
	M[y][x] = 2

	// go RIGHT
	for i := x + 1; i < len(M[0]); i++ {
		if M[y][i] == 5 {
			break
		}
		if M[y][i] == 0 {
			M[y][i] = 1
		}
	}

	// go LEFT
	for i := x - 1; i >= 0; i-- {
		if M[y][i] == 5 {
			break
		}
		if M[y][i] == 0 {
			M[y][i] = 1
		}
	}

	// go UP
	for i := y + 1; i < len(M); i++ {
		if M[i][x] == 5 {
			break
		}
		if M[i][x] == 0 {
			M[i][x] = 1
		}
	}

	// go DOWN
	for i := y - 1; i >= 0; i-- {
		if M[i][x] == 5 {
			break
		}
		if M[i][x] == 0 {
			M[i][x] = 1
		}
	}

	// go RIGHT-UP
	for i, j := x+1, y-1; i < len(M[0]) && j >= 0; {
		if M[j][i] == 5 {
			break
		}
		if M[j][i] == 0 {
			M[j][i] = 1
		}
		i++
		j--
	}

	// go RIGHT-DOWN
	for i, j := x+1, y+1; i < len(M[0]) && j < len(M); {
		if M[j][i] == 5 {
			break
		}
		if M[j][i] == 0 {
			M[j][i] = 1
		}
		i++
		j++
	}

	// go LEFT-DOWN
	for i, j := x-1, y+1; i >= 0 && j < len(M); {
		if M[j][i] == 5 {
			break
		}
		if M[j][i] == 0 {
			M[j][i] = 1
		}
		i--
		j++
	}

	// go LEFT-UP
	for i, j := x-1, y-1; i >= 0 && j >= 0; {
		if M[j][i] == 5 {
			break
		}
		if M[j][i] == 0 {
			M[j][i] = 1
		}
		i--
		j--
	}

	q_pos := []int{}
	for i := 0; i < len(M); i++ {
		for j := 0; j < len(M[0]); j++ {
			if M[i][j] == 2 {
				q_pos = append(q_pos, i*len(M[0])+j)
			}
		}
	}
	return arr_string(q_pos)
}

func exploreBoard(M [][]rune) {
	for i := 0; i < len(M); i++ {
		for j := 0; j < len(M[0]); j++ {
			if M[i][j] == 0 {
				M1 := copyPosition(M)
				pos := putQueen(M1, i, j)
				if !global_map[pos] {
					global_map[pos] = true
					exploreBoard(M1)
				}
			}
		}
	}
}

func positionOfComponent(M [][]rune) (bool, int, int) {
	for i := 0; i < len(M); i++ {
		for j := 0; j < len(M[0]); j++ {
			if M[i][j] == 0 {
				return true, i, j
			}
		}
	}
	return false, -1, -1
}

func extractComponent(M [][]rune, y, x int) {
	frontier := [][2]int{[2]int{y, x}}
	seen := map[[2]int]bool{[2]int{y, x}: true}

	for len(frontier) > 0 {
		new_frontier := [][2]int{}
		for _, v := range frontier {
			i, j := v[0], v[1]
			M[i][j] = 2
			neighbors := [][2]int{
				[2]int{i, j + 1},
				[2]int{i + 1, j + 1},
				[2]int{i + 1, j},
				[2]int{i + 1, j - 1},
			}
			for _, el := range neighbors {
				i_1, j_1 := el[0], el[1]
				if i_1 >= 0 && i_1 < len(M) && j_1 >= 0 && j_1 < len(M[0]) {
					if M[i_1][j_1] == 0 && !seen[[2]int{i_1, j_1}] {
						seen[[2]int{i_1, j_1}] = true
						new_frontier = append(new_frontier, [2]int{i_1, j_1})
					}
				}
			}
		}
		frontier = new_frontier
	}

}

func divideIntoComponents(M [][]rune) {
	for {
		is_found, _, _ := positionOfComponent(M)
		if !is_found {
			return
		}
	}
}

func main() {
	//	reader, T := bufio.NewReader(os.Stdin), 0
	//
	//	for fmt.Scanf("%d", &T); T > 0; T-- {
	//		text, _ := reader.ReadString('\n')
	//		tmp := [2]int{0, 0}
	//		for pos, v := range strings.Fields(text) {
	//			num, _ := strconv.Atoi(v)
	//			tmp[pos] = num
	//		}
	//
	//		row, col := tmp[0], tmp[1]
	//		M := make([][]int, row)
	//		a := make([]int, row * col)
	//		for i := range M {
	//			M[i] = a[i * col:(i + 1) * col]
	//		}
	//
	//		for i := 0; i < row; i++ {
	//			text, _ := reader.ReadString('\n')
	//			for j := 0; j < col; j++ {
	//				if text[j] == '#' {
	//					M[i][j] = 5
	//				}
	//			}
	//		}
	//
	//		global_map = make(map[string]bool)
	//		exploreBoard(M)
	//		fmt.Println(len(global_map))
	//	}

	M := [][]rune{
		[]rune{0, 0},
		[]rune{0, 0},
		[]rune{5, 5},
		[]rune{0, 0},
		[]rune{5, 0},
		[]rune{5, 0},
		[]rune{0, 5},
		[]rune{5, 5},
		[]rune{5, 5},
		[]rune{0, 5},
		[]rune{0, 0},
		[]rune{5, 5},
		[]rune{5, 0},
	}
	//	divideIntoComponents(M)
	extractComponent(M, 0, 0)

	//	start := time.Now()
	//	exploreBoard(M)
	//	fmt.Println(len(global_map))
	//	elapsed := time.Since(start)
	//	fmt.Println(elapsed)
}
