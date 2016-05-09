// Never user NewScanner! It has a limit on the number of characters it can read. Use NewReader
// append is bad, preallocate if you can. At least 4 times slower
package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

// Numbers, pairs, triples
func readManyNumbers() []int {
	/*
		read many numbers. Each of them is on another line

		3 		number of numbers
		5		first number
		2		second number
		18		third number
	*/
	T := 0
	fmt.Scanf("%d", &T)

	reader, numbers := bufio.NewReader(os.Stdin), make([]int, T)
	for i := 0; i < T; i++ {
		text, _ := reader.ReadString('\n')
		num, _ := strconv.Atoi(strings.TrimRight(text, "\n"))
		numbers[i] = num
	}
	return numbers
}

func readManyPairs() [][2]int {
	/*
		read many pairs of numbers

		3		number of pairs
		3 2
		4 6
		5 7
	*/
	T := 0
	fmt.Scanf("%d", &T)

	reader, pairs := bufio.NewReader(os.Stdin), make([][2]int, T)
	for i := 0; i < T; i++ {
		text, _ := reader.ReadString('\n')
		tmp := [2]int{0, 0}
		for pos, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			tmp[pos] = num
		}
		pairs[i] = tmp
	}
	return pairs
}

// Arrays
func readOneArray() []int {
	/*
		Read array of numbers of the form

		5 					length of array
		1 2 15 12 65		actual array
	*/
	T := 0
	fmt.Scanf("%d", &T)

	reader, arr := bufio.NewReader(os.Stdin), make([]int, T)
	text, _ := reader.ReadString('\n')
	for i, v := range strings.Fields(text) {
		num, _ := strconv.Atoi(v)
		arr[i] = num
	}
	return arr
}

func readTwoArrays() ([]int, []int) {
	/*
		Read two arrays of numbers of the form

		5 					length of array
		1 2 15 12 65		actual array
		8 1 5 9 52			actual array
	*/
	T := 0
	fmt.Scanf("%d", &T)

	reader := bufio.NewReader(os.Stdin)
	arr1, arr2 := make([]int, T), make([]int, T)

	text, _ := reader.ReadString('\n')
	for i, v := range strings.Fields(text) {
		num, _ := strconv.Atoi(v)
		arr1[i] = num
	}

	text, _ = reader.ReadString('\n')
	for i, v := range strings.Fields(text) {
		num, _ := strconv.Atoi(v)
		arr2[i] = num
	}

	return arr1, arr2
}

func readManyArraysOfSameLength() [][]int {
	// TODO have not finished
	/*
		read many arrays, each of which has the same number of elements

		2				number of arrays
		1 2 3 4			first array
		1 2	5 1			second array
	*/
	T, reader, res := 0, bufio.NewReader(os.Stdin), [][]int{}
	for fmt.Scanf("%d", &T); T > 0; T-- {
		text, _ := reader.ReadString('\n')
		arr := []int{}
		for _, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			arr = append(arr, num)
		}
		res = append(res, arr)
	}
	return res
}

func readManyArraysOfDifferentLength() {
	/*
		read many arrays in the following format

		2			number of arrays
		4			length of the array
		1 2 3 4		actual array
		2			another length
		1 2			actual array
	*/
	T, reader := 0, bufio.NewReader(os.Stdin)
	for fmt.Scanf("%d", &T); T > 0; T-- {
		text, _ := reader.ReadString('\n')
		num, _ := strconv.Atoi(strings.TrimRight(text, "\n"))

		// try this next time
		// text, _ := reader.ReadString('\r')
		// num, _ := strconv.Atoi(strings.Trim(text, "\n\r"))
		arr := make([]int, num)

		text, _ = reader.ReadString('\n') // '\r'
		for i, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			arr[i] = num
		}
		// fmt.Println(arr)
	}
}

func readManyArraysOfDifferentLengthWithSpecialNumber() {
	/*
		read many array which looks like

		2				number of arrays
		4 5				length of the array and some Important number
		1 2 3 4			first array
		2 7				another length and some Important number
		1 2 6 7 9 1 	second array
	*/
	T, reader := 0, bufio.NewReader(os.Stdin)
	for fmt.Scanf("%d", &T); T > 0; T-- {
		text, _ := reader.ReadString('\n')

		tmp := [2]int{}
		for i, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			tmp[i] = num
		}

		arr := make([]int, tmp[0])
		text, _ = reader.ReadString('\n')
		for i, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			arr[i] = num
		}

		fmt.Println(arr, tmp[1])
	}
}

// Other stuff

func readMatrix() [][]uint64 {
	// TODO improve
	/*
		Read matrix of the form

		1 2 3 4
		5 6 7 8
		9 1 2 3
	*/
	linesNum, reader, matrix := 0, bufio.NewReader(os.Stdin), [][]uint64{}
	fmt.Scanf("%d", &linesNum)
	for i := 0; i < linesNum; i++ {
		text, _ := reader.ReadString('\n')
		line := []uint64{}
		for _, v := range strings.Fields(text) {
			num, _ := strconv.Atoi(v)
			line = append(line, uint64(num))
		}
		matrix = append(matrix, line)
	}
	return matrix
}

func readBooleanGrid() [][]bool {
	/*
		Read boolean matrix, where one character means True ('.') another one is False

		4 5
		.....
		.x.x.
		.....
		.....
	*/
	row, col, reader := 0, 0, bufio.NewReader(os.Stdin)
	fmt.Scanf("%d %d", &row, &col)

	M := make([][]bool, row)
	a := make([]bool, row*col)
	for i := range M {
		M[i] = a[i*col : (i+1)*col]
	}

	for i := 0; i < row; i++ {
		text, _ := reader.ReadString('\n')
		for j := 0; j < col; j++ {
			if text[j] == '.' {
				M[i][j] = true
			}
		}
	}
	return M
}

func readManyBooleanGrids() {
	/*
		Read boolean matrix, where one character means True ('.') another one is False
		3			number of boolean grids
		3 3			dims of the first one
		...
		...
		...
		3 3			dims of the second one
		.#.
		.#.
		...
		2 4			dims of the third one
		.#..
		....
	*/
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
		a := make([]int, row*col)
		for i := range M {
			M[i] = a[i*col : (i+1)*col]
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

func readDirectionsGrid() [][]int {
	/*
		Read a grid of U, D, L, R points and transform it into a matrix
		2 2		Dimensions
		RD
		*L
	*/
	row, col, reader := 0, 0, bufio.NewReader(os.Stdin)
	fmt.Scanf("%d %d", &row, &col)

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
	return M
}

func readLinesOfStrings() []string {
	// TODO improve
	/*
		Read lines of strings

		3
		string_one
		another
		string
	*/
	reader, arr, T := bufio.NewReader(os.Stdin), []string{}, 0
	fmt.Scanf("%d", &T)
	for ; T > 0; T-- {
		text, _ := reader.ReadString('\n')
		arr = append(arr, text)
	}
	return arr
}

// Graphs and trees
func readWeightedTree() (map[int][]int, []int) {
	// TODO improve
	/*
		6							// N number of vertices
		100 200 100 500 100 600		// weights of the tree
		1 2							// tree. All vertices are from 1 to N
		2 3
		2 5
		4 5
		5 6
	*/
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

// TODO improve
func readUndirectedUnweightedGraphFromEdgeList() map[int]map[int]bool {
	scanner := bufio.NewScanner(os.Stdin)
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
		G[num2][num1], G[num1][num2] = true, true
	}
	return G
}

func readDirectedUnweightedGraphFromConnectivityList() map[int]map[int]bool {
	// https://www.hackerrank.com/challenges/dfsprobreach
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	N, _ := strconv.Atoi(scanner.Text())
	G := map[int]map[int]bool{}
	for n := 1; n <= N+1; n++ {
		scanner.Scan()
		arr := strings.Fields(scanner.Text())
		G[n] = map[int]bool{}
		for i := 1; i < len(arr); i++ {
			v, _ := strconv.Atoi(arr[i])
			G[n][v] = true
		}
	}
	return G
}

func readUndirectedWeightedGraphFromEdgeList() map[int]map[int]int {
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
		if len(G[num2]) == 0 {
			G[num2] = map[int]int{}
		}
		G[num2][num1], G[num1][num2] = weight, weight
	}
	return G
}

func readDirectedWeightedGraphFromEdgeList() map[int]map[int]int {
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
	return G
}

// Write to the terminal
func writeManyNumbers(numbers []int) {
	var buffer bytes.Buffer
	for _, v := range numbers {
		buffer.WriteString(strconv.Itoa(v) + "\n")
	}
	fmt.Print(buffer.String())
}
