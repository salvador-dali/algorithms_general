package main

import (
	"fmt"
)

func giveSolution(n, k int) ([]int, bool) {
	seen, res := map[int]bool{}, make([][]int, n)

	for i := 1; i < n+1; i++ {
		v1, v2, possible := i+k, i-k, []int{}
		if v1 <= n && !seen[v1] {
			possible = append(possible, v1)
		}

		if v2 > 0 && !seen[v2] {
			possible = append(possible, v2)
		}

		if len(possible) == 0 {
			return []int{}, false
		}

		if len(possible) == 1 {
			seen[possible[0]] = true
		}
		res[i-1] = possible
	}

	// res holds a crude solution. Refine it
	res_refined := make([]int, n)
	for i := n - 1; i >= 0; i-- {
		if len(res[i]) == 2 {
			possible := []int{}
			for _, v := range res[i] {
				if !seen[v] {
					possible = append(possible, v)
				}
			}

			if len(possible) == 0 {
				return []int{}, false
			}

			if len(possible) == 1 {
				seen[possible[0]] = true
				res_refined[i] = possible[0]
			}
		} else {
			res_refined[i] = res[i][0]
		}
	}

	return res_refined, true
}

func abs(n, k int) ([]int, bool) {
	if k == 0 {
		res := make([]int, n)
		for i := 1; i <= n; i++ {
			res[i-1] = i
		}
		return res, true
	}

	if n%2 == 1 {
		return []int{}, false
	}

	if k > n/2 {
		return []int{}, false
	}

	return giveSolution(n, k)
}

func printArray(arr []int) {
	for _, v := range arr[:len(arr) - 1] {
		fmt.Print(v, " ")
	}
	fmt.Println(arr[len(arr) - 1])
}

func main() {
	T, n, k := 0, 0, 0
	fmt.Scanf("%d", &T)

	for i := 0; i < T; i++ {
		fmt.Scanf("%d %d", &n, &k)
		res, ok := abs(n, k)
		if !ok {
			fmt.Println(-1)
		} else {
			printArray(res)
		}
	}
}
