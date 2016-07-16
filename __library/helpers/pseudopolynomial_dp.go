package main

import (
	"fmt"
)

func partition_problem(arr []int) bool {
	// https://en.wikipedia.org/wiki/Partition_problem
	s := 0
	for _, v := range arr {
		s += v
	}

	if s%2 == 1 {
		return false
	}

	row, col := s/2+1, len(arr)+1
	M := make([][]bool, row)
	e := make([]bool, row*col)
	for i := range M {
		M[i] = e[i*col : (i+1)*col]
	}

	for i := 0; i < col; i++ {
		M[0][i] = true
	}

	for i := 1; i < row; i++ {
		for j := 1; j < col; j++ {
			M[i][j] = M[i][j-1]
			if i >= arr[j-1] {
				M[i][j] = M[i][j] || M[i-arr[j-1]][j-1]
			}
		}
	}

	return M[row-1][col-1]
}

func knapsack_0_1(values []int, weights []int, maxW int) int {
	/**
	dynamic programming implementation of knapsack
	http://www.cs.rit.edu/~zjb/courses/800/lec7.pdf
	knapsack([]int{1, 6, 18, 22, 28}, []int{1, 2, 5, 6, 7}, 11)
	*/
	if len(values) != len(weights) {
		panic("values and weights should be the same length")
	}

	row, col := len(values)+1, maxW+1

	M := make([][]int, row)
	e := make([]int, row*col)
	for i := range M {
		M[i] = e[i*col : (i+1)*col]
	}

	for i := 1; i < row; i++ {
		for w := 0; w < col; w++ {
			tmp := values[i-1] + M[i-1][w-weights[i-1]]
			if weights[i-1] <= w && tmp > M[i-1][w] {
				M[i][w] = tmp
			} else {
				M[i][w] = M[i-1][w]
			}
		}
	}

	return M[len(values)][maxW]
}

func knapsack_unbounded(prices []int, goal int) int {
	// https://www.hackerrank.com/challenges/unbounded-knapsack/
	sort.Ints(prices)
	arr, n, prev := make([]int, len(prices)), 0, -1
	for _, v := range prices {
		if v != prev {
			if goal%v == 0 {
				return goal
			}
			arr[n], prev, n = v, v, n+1
		}
	}

	prices = arr[:n]

	row, col := goal+1, n+1
	M := make([][]bool, row)
	e := make([]bool, row*col)
	for i := range M {
		M[i] = e[i*col : (i+1)*col]
	}

	for i := 0; i < col; i++ {
		M[0][i] = true
	}

	for i := 1; i < row; i++ {
		for j := 1; j < col; j++ {
			M[i][j] = M[i][j-1]
			if i >= prices[j-1] {
				M[i][j] = M[i][j] || M[i-prices[j-1]][j]
			}
		}
	}

	for i := row - 1; i >= 0; i-- {
		if M[i][col-1] {
			return i
		}
	}

	return 0
}

func main() {

}
