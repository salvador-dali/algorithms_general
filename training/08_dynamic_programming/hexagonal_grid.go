// https://www.hackerrank.com/challenges/hexagonal-grid
package main

import (
	"fmt"
)

func analyse(arr1, arr2 []bool) bool {
	cnt, n := 0, len(arr1)
	for i := 0; i < n; i++ {
		if !arr1[i] {
			cnt++
		}
		if !arr2[i] {
			cnt++
		}
	}
	if cnt%2 == 1 {
		return false
	}

	for i := 0; i < n-1; i++ {
		if !arr1[i] {
			cnt++
		}
		if !arr2[i] {
			cnt++
		}

		if arr2[i] && arr1[i+1] && cnt%2 == 1 {
			return false
		}

		if arr2[i] && arr1[i] && cnt%2 == 1 {
			return false
		}
	}
	return true
}

func main() {
	T, n, s1, s2 := 0, 0, "", ""
	for fmt.Scanf("%d", &T); T > 0; T-- {
		fmt.Scanf("%d", &n)
		fmt.Scanf("%s", &s1)
		fmt.Scanf("%s", &s2)
		arr1, arr2 := make([]bool, n), make([]bool, n)
		for i := 0; i < n; i++ {
			if s1[i] == '1' {
				arr1[i] = true
			}

			if s2[i] == '1' {
				arr2[i] = true
			}
		}

		if analyse(arr1, arr2) {
			fmt.Println("YES")
		} else {
			fmt.Println("NO")
		}
	}
}
