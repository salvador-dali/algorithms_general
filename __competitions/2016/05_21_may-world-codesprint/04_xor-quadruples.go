package main

import (
	"fmt"
	"sort"
	"time"
)

func calc(a, b, c, d int) {
	arr := []int{a, b, c, d}
	sort.Ints(arr)
	a, b, c, d = arr[0], arr[1], arr[2], arr[3]

	cnt, seen := 0, map[[4]int]bool{}
	for w := 1; w <= a; w++ {
		for x := w; x <= b; x++ {
			for y := x; y <= c; y++ {
				for z := y; z <= d; z++ {
					res := w ^ x ^ y ^ z
					tmp := []int{w, x, y, z}
					sort.Ints(tmp)

					tpl := [4]int{tmp[0], tmp[1], tmp[2], tmp[3]}

					if res != 0 && !seen[tpl]{
						seen[tpl] = true
						cnt++
					}
				}
			}
		}
	}
	fmt.Println(cnt)
}

func main() {
	a, b, c, d := 0, 0, 0, 0
	fmt.Scanf("%d %d %d %d", &a, &b, &c, &d)

	start := time.Now()
	calc(a, b, c, d)
	fmt.Println(time.Since(start))

}
