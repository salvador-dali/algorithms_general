// http://e-maxx-eng.github.io/data_structures/fenwick.html
//http://arxiv.org/pdf/1311.6093.pdf
package main
import (
	"fmt"
)

func update(arr [][]int, x, y, value int){
	for i := x; i < len(arr[0]); i = i | (i+1){
		for j := y; j < len(arr); j = j | (j+1){
			arr[i][j] += value;
		}
	}
}

func prefix(arr [][]int, x, y int)int{
	s := 0
	for i := x; i >= 0; i = i & (i+1) - 1 {
		for j := y; j >= 0; j = j & (j+1) - 1 {
			s += arr[i][j]
		}
	}
	return s
}

func main(){
	x, y := 5, 6
	arr := [][]int{}
	for i := 0; i <= y; i++{
		arr = append(arr, make([]int, x + 1))
	}

	update(arr, 1, 1, 2)
	update(arr, 1, 5, 5)
	update(arr, 1, 4, 1)
	update(arr, 2, 3, -2)
	update(arr, 2, 2, 4)
	update(arr, 3, 1, 4)
	update(arr, 3, 2, 3)
	update(arr, 3, 4, 1)
	update(arr, 4, 3, -6)
	update(arr, 4, 5, 3)
	update(arr, 5, 1, 3)
	update(arr, 6, 2, 1)
	update(arr, 6, 5, 1)


	fmt.Println(prefix(arr, 5, 2))
}
