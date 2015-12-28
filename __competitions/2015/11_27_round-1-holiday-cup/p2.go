// https://www.hackerrank.com/contests/round-1-holiday-cup/challenges/ternarian-weights
package main
import (
	"strconv"
	"fmt"
	"bufio"
	"os"
)

func readManyNumbers() []uint64 {
	var T int
	fmt.Scanf("%d", &T)

	scanner, numbers := bufio.NewScanner(os.Stdin), []uint64{}
	for T > 0 {
		T--
		scanner.Scan()
		num, _ := strconv.Atoi(scanner.Text())
		numbers = append(numbers, uint64(num))
	}
	return numbers
}

func convertToTernary(n uint64) []int {
	zero, one, three := uint64(0), uint64(1), uint64(3)
	if n == zero {
		return []int{}
	}

	mod := n % three
	if mod == zero {
		return append([]int{0}, convertToTernary(n / three)...)
	}

	if mod == one {
		return append([]int{1}, convertToTernary(n / three)...)
	}

	return append([]int{-1}, convertToTernary((n + one) /three)...)
}

func output(arr []int) ([]uint64, []uint64){
	right, left := []uint64{}, []uint64{}
	val := uint64(1)
	for _, v := range arr {
		if v == 1 {
			right = append([]uint64{val}, right...)
		} else if v == -1 {
			left = append([]uint64{val}, left...)
		}

		val *= uint64(3)
	}

	return right, left
}

func print(right, left []uint64){
	fmt.Printf("left pan:")
	for _, v := range left {
		fmt.Printf(" %d", v)
	}
	fmt.Println()
	fmt.Printf("right pan:")
	for _, v := range right {
		fmt.Printf(" %d", v)
	}
	fmt.Println()
	fmt.Println()
}

func main(){
	numbers := readManyNumbers()
	for _, v := range numbers{
		arr := convertToTernary(v)
		right, left := output(arr)
		print(right, left)
	}
}


//http://rosettacode.org/wiki/Balanced_ternary#Python
//https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=golang%20print%20array%20without%20brackets
//https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=balanced%20ternary%20python
