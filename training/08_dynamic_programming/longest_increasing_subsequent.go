//https://www.hackerrank.com/challenges/longest-increasing-subsequent/
package main
import (
	"fmt"
	"bufio"
	"os"
	"strconv"
	"strings"
)

func bisect_left(arr []int, n int) int {
	lo, hi := 0, len(arr)
	for ; hi > lo; {
		mid := lo + (hi - lo) / 2
		if arr[mid] >= n {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}

func patience(arr []int) int {
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


func readManyNumbers() []int {
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

func main(){
	fmt.Println(patience(readManyNumbers()))
}
