package main

import (
	"fmt"
)

func bisect_left(arr []int, n int) int {
	lo, hi := 0, len(arr)
	for hi > lo {
		mid := lo + (hi-lo)/2
		if arr[mid] >= n {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}

func isPalindrome(s string) bool {
	/**
	checks whether the string is a palindrome with O(n/2)
	*/
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-i-1] {
			return false
		}
	}
	return true
}

func longestCommonSubstring(s1, s2 string) int {
	// Get some improvements from
	// https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence
	n1, n2 := len(s1), len(s2)

	M := make([][]int, n2+1)
	e := make([]int, (n2+1)*(n1+1))
	for i := range M {
		M[i] = e[i*(n1+1) : (i+1)*(n1+1)]
	}

	for i := 1; i <= n2; i++ {
		for j := 1; j <= n1; j++ {
			if s1[j-1] == s2[i-1] {
				M[i][j] = M[i-1][j-1] + 1
			} else if M[i-1][j] < M[i][j-1] {
				M[i][j] = M[i][j-1]
			} else {
				M[i][j] = M[i-1][j]
			}
		}
	}

	return M[n2][n1]
}

func longestIncreasingSubsequence([]int) int {
	// almost twice as fast as the one with sort.SearchInts instead of bisect_left
	// preallocation of an array takes piles_top := make([]int, len(arr)) decreases allocations to 1
	// but hugely increases B/op
	// https://www.hackerrank.com/challenges/longest-increasing-subsequent
	// to get the sequence
	// https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence.pdf
	// http://wordaligned.org/articles/patience-sort
	piles_top := []int{}
	for _, v := range arr {
		pos := bisect_left(piles_top, v)
		if len(piles_top) == pos {
			piles_top = append(piles_top, v)
		} else {
			piles_top[pos] = v
		}
	}

	return len(piles_top)
}
