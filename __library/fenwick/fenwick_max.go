package main
import (
	"fmt"
)

/**
 you have an array of N elements, and many queries to find
 - maximum in the interval
 - increase the value by some positive number
 */
func max(a, b int)int{
	if a > b{
		return a
	}
	return b
}

func update(arr, left, right []int, index, value int){
	arr[index - 1] = value
	for i := index; i <= 8; {
		left[i] = max(left[i], value)
		i = i + i - (i & (i-1))
	}

	for i := index; i > 0; {
		right[i] = max(right[i], value)
        i = i - i - (i & (i-1))
	}
}

func getMax(arr, left, right []int, l, r int)int{
	res, i := 0, l

	for i + i - (i & (i-1)) <= r {
		res = max(res, right[i])
		i = i + i - (i & (i-1))
	}


  	// if arr[i - 1] > res { ans := 1}

	res = max(res, arr[i - 1])
    i = r

    for i - i - (i & (i-1)) >= l {
        res = max(res, left[i])
        i = i - i - (i & (i-1))
    }

    return res
}

func main(){
	n := 10
	arr := make([]int, n + 1)
	left := make([]int, n + 1)
	right := make([]int, n + 1)
	update(arr, left, right, 2, 2)
	update(arr, left, right, 1, 3)
	update(arr, left, right, 3, 1)
	update(arr, left, right, 4, 7)
	update(arr, left, right, 5, 3)
	update(arr, left, right, 7, 1)
	update(arr, left, right, 8, 9)
	update(arr, left, right, 9, 3)
	update(arr, left, right, 10, 2)

	for i := 1; i <= 10; i++{
		for j := i; j <= 10; j++{
			fmt.Println("[", i, j, "]", getMax(arr, left, right, i, j))
		}
	}
}
