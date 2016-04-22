// https://www.hackerrank.com/challenges/taum-and-bday
package main

import "fmt"

func main() {
	T := 0
	fmt.Scanf("%d", &T)
	for T > 0 {
		T--
		var w, b, x, y, z uint64
		fmt.Scanf("%d %d", &b, &w)
		fmt.Scanf("%d %d %d", &x, &y, &z)

		arr := []uint64{b*x + w*y, (b+w)*x + w*z, (b+w)*y + b*z}
		min := arr[0]
		for i := 1; i < len(arr); i++ {
			if arr[i] < min {
				min = arr[i]
			}
		}

		fmt.Println(min)
	}
}
